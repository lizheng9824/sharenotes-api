from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import dbconfig

user = dbconfig.DB_USER
password = dbconfig.PASSWORD
host = dbconfig.HOST
db_name = dbconfig.DATABASE

engine = create_engine(
    f'mysql+mysqlconnector://{user}:{password}@{host}/{db_name}')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
