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

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)


def add_record(name, full_name, nick_name):
    record = User(name=name, fullname=full_name, nickname=nick_name)

    with Session() as session:
        session.add(record)
        session.commit()


def get_all_records_by_id(name):
    with Session() as session:
        our_user = session.query(User).filter_by(name=name).all()
    return our_user
