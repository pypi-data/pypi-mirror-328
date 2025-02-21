from datetime import datetime
from pathlib import Path

from sqlalchemy import text
from sqlmodel import SQLModel, Field, Session, select


class Migration(SQLModel, table=True):
    filename: str = Field(default=None, primary_key=True, nullable=False)
    executed_at: datetime = Field(default=datetime.now(), nullable=False)


class SQLMigrationExecutor:
    def __init__(self, session: Session, path: Path | str):
        self.session: Session = session
        self.path: Path = Path(path)

    def run(self) -> list[Migration]:
        pending_migrations_stack: list[Path] = [Path(file) for file in (self.path / 'migrations').glob("*.sql")]
        pending_migrations_stack.sort()  # guarantee the execution order of the sql files based in their filenames

        migrations: list[Migration] = [self._execute(migration_file) for migration_file in pending_migrations_stack]
        self.session.close()

        return migrations

    def _execute(self, sql_file: Path) -> Migration:
        # noinspection PyTypeChecker
        last_execution: datetime | None = self.session.exec(select(Migration).where(Migration.filename == sql_file.name)).first()
        migration: Migration | None = None

        if last_execution:
            # Return the last migration executed
            migration = Migration(filename=sql_file.name, executed_at=last_execution)
        else:
            # Read the file and execute the sql statements
            with sql_file.open(mode="r", encoding="utf-8") as file:
                try:
                    # Get all statements from the file and execute each one sequentially
                    statements: list[str] = [statement.strip() for statement in file.read().split(";")
                                             if isinstance(statement, str) and statement.strip() != '']

                    while statements:
                        statement: str = statements.pop(0)  # use the list as a queue for performance
                        self.session.execute(text(statement))

                    migration = Migration(filename=sql_file.name)
                    self.session.add(migration)

                    self.session.commit()
                except Exception as e:
                    self.session.rollback()
                    raise RuntimeError(f"Error executing migration {file}: {str(e)}")

        return migration
