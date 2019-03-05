from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'postgresql://rohan@localhost/postgres', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()

class Verse(Base):
    __tablename__ = 'rv'
    id = Column(Integer, primary_key=True)
    sect = Column(SmallInteger)
    page = Column(SmallInteger)
    verse = Column(SmallInteger)
    dev = Column(Text)
    rom = Column(Text)
    eng = Column(Text)
