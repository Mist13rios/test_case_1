from settings import Base
from sqlalchemy import Column, Integer, String


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    nickname = Column(String)
    email = Column(String)

    def __repr__(self):
        return "<User(first_name='%s', last_name='%s', nickname='%s')>" % (
            self.first_name,
            self.last_name,
            self.nickname
        )
