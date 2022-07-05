import json

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from pathlib import Path
cur_dir = Path(__file__).parent
path_to_db = cur_dir.joinpath('local_db.db')
engine = create_engine(f'sqlite:///{path_to_db}', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    # def __repr__(self):
    #     return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)

def add_record(name, full_name, nick_name):
    record = User(name=name, fullname=full_name, nickname=nick_name)

    with Session() as session:
        session.add(record)
        session.commit()


def get_all_records_by_id(driver_name, plate_number, list_number):
    if not driver_name:
        driver_name = "0"
    data = {}
    # TODO provide check for all values
    with Session() as session:
        our_user = session.query(User).filter_by(name=driver_name).all()
    if our_user:
        for i, user in enumerate(our_user):
            data[i] = {"user_name": user.name, "last name": user.fullname }

    return data


if __name__ == "__main__":
    obj = get_all_records_by_id(None, None, None)
    # print(type(obj.name))
    print(type(obj))
    print(obj)