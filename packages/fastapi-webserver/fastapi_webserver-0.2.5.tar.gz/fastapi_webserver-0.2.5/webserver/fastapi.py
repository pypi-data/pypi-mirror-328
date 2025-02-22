from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.templating import Jinja2Templates

from webserver import config

settings: config.Settings
app: FastAPI
templates: Jinja2Templates | None = None

def _custom_generate_unique_id(route: APIRoute) -> str:
    """
    Generate a unique ID for the client side generation.
    Source: https://fastapi.tiangolo.com/advanced/generate-clients/#custom-operation-ids-and-better-method-names
    :return: route id
    """
    if route.tags:
        return f"{route.tags[0]}-{route.name}"
    else:
        return f"{route.name}"


@asynccontextmanager
async def _lifespan(app: FastAPI):
    """Manages the lifespan of a FastAPI application."""
    from webserver.commons import db, runtime

    # startup
    runtime.import_modules(settings.MODULES)  # Load modules to allow orm metadada creation

    db.setup_db()
    yield
    # shutdown

# ------

settings: config.Settings = config.settings

app = FastAPI(
    title=settings.APP_NAME,
    openapi_url=f"{settings.HTTP_ROOT_PATH}openapi.json",
    generate_unique_id_function=_custom_generate_unique_id,
    lifespan=_lifespan
)

if settings.http_static_enabled:
    from starlette.staticfiles import StaticFiles
    app.mount("/static", StaticFiles(directory=str(settings.static_folder.resolve())))

if settings.templates_enabled:
    templates = Jinja2Templates(directory=str(settings.templates_folder.resolve()))

# Set all CORS enabled origins
if settings.CORS_ORIGINS:
    from starlette.middleware.cors import CORSMiddleware

    # noinspection PyTypeChecker
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# SSL
if settings.enable_ssl:
    if not settings.SSL_CERTIFICATE and not settings.SSL_PRIVATE_KEY:
        certs_folder: Path = Path(settings.RESOURCES_FOLDER / 'certs')

        cert = (certs_folder / f"{settings.HOST}.pem")
        key = (certs_folder / f"{settings.HOST}-key.pem")

        if cert.exists() and key.exists():
            # assign existent certificates to the environment variable
            settings.SSL_CERTIFICATE = str(cert.resolve())
            settings.SSL_PRIVATE_KEY = str(key.resolve())
        else:
            # generates a certificate
            from webserver.commons.net.certs import get_cert

            files = get_cert(certs_folder, [settings.HOST])
            settings.SSL_CERTIFICATE = str(files.cert.resolve())
            settings.SSL_PRIVATE_KEY = str(files.key.resolve())

def start():
    """
    Start a local uvicorn server.
    """
    import uvicorn
    if settings.enable_ssl:
        uvicorn.run(app, host=settings.HOST, port=8000,
                    ssl_certfile=settings.ssl_certificate.resolve(),
                    ssl_keyfile=settings.ssl_private_key.resolve())
    else:
        uvicorn.run(app, host=settings.HOST, port=8000)

