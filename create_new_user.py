from models import User
from settings import Session

session = Session()

SingleUser = User('test@test.ru', 'test', 'John', 'Cena')
session.add(SingleUser)
session.commit()
