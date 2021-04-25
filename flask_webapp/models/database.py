from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE = "mysql://%s:%s@%s/%s?charset=utf8mb4" % (
    "root",
    "P@ssw0rd",
    "127.0.0.1:3306",
    "mydb",
)
ENGINE = create_engine(DATABASE, convert_unicode=True, echo=True)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))

Base = declarative_base()
Base.query = session.query_property()


def init_db():
    import models.models

    Base.metadata.create_all(bind=ENGINE)
