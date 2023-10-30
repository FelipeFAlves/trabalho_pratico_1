from sqlalchemy import *
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, sessionmaker

from db import *

def create_model():
    engine = make_engine()
    base = automap_base()
    base.prepare(engine, schema='public')
    # print(base.classes.keys())
    return base
    

def make_engine():
    return create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/dvdrental_orm', echo=False)