from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import MYSQL_URI

engine = create_engine(MYSQL_URI)

Base = declarative_base(bind=engine)
DBSession = sessionmaker(bind=engine)
