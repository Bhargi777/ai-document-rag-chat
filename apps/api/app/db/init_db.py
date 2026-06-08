from app.db.session import engine
from app.db.base import create_db_tables


def initialize_database() -> None:
    create_db_tables(engine)
