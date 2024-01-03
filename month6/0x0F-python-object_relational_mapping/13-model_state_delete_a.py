#!/usr/bin/python3
"""13. Delete states
"""
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State)\
        .filter(func.binary(State.name).like('%a%')).all()
    [session.delete(row) for row in rows]
    session.commit()
