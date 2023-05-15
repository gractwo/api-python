import os
from functools import cache

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


@cache
def db_session() -> scoped_session:
    engine = create_engine(os.environ["DB_CONNECTION_STRING"])
    session_factory = sessionmaker(bind=engine)
    return scoped_session(session_factory)
