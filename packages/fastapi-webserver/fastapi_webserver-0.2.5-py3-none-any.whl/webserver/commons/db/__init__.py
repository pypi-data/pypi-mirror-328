from typing import Generator, Annotated

from fastapi import Depends
from sqlmodel import Session

from .adapter import DatabaseAdapter
from .migration import DatabaseMigrationExecutor


def session(**kwargs) -> Session:
    from webserver.config import settings
    return Session(settings.database_adapter.engine(), **kwargs)


def setup_db():
    from sqlmodel import SQLModel
    from webserver.config import settings

    if settings.has_database:
        # Create DB and Tables via ORM
        SQLModel.metadata.create_all(settings.database_adapter.engine())

        # Migrate SQL Data
        with session() as s:
            DatabaseMigrationExecutor(path=settings.resources_folder / "migrations", session=s).run()
            s.close()


def _fastapi_generate_db_session() -> Generator[Session]:
    s: Session = session()

    try:
        yield s
    finally:
        s.close()

# Sets a session as dependency
DatabaseSessionDependency = Annotated[Session, Depends(_fastapi_generate_db_session)]

