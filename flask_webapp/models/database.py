from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import configparser

config_ini = configparser.ConfigParser()
config_ini.read("models/config.ini", encoding="utf-8")

db_user = config_ini["DATABASE"]["user"]
db_password = config_ini["DATABASE"]["password"]
db_ip = config_ini["DATABASE"]["ip"]
db_name = config_ini["DATABASE"]["db_name"]

DATABASE = "mysql://%s:%s@%s/%s?charset=utf8mb4" % (
    db_user,
    db_password,
    db_ip,
    db_name,
)
ENGINE = create_engine(DATABASE, convert_unicode=True, echo=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models.models

    Base.metadata.create_all(bind=ENGINE)
