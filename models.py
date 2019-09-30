from settings import Base
from sqlalchemy import Column, Integer, String


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, email, password, first_name, last_name):
        self.email = email,
        self.password = password,
        self.first_name = first_name,
        self.last_name = last_name

    def __repr__(self):
        return "<User(first_name='%s', last_name='%s')>" % (
            self.first_name,
            self.last_name,
        )
