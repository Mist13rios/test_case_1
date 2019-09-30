from local_values.reader import env_value
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://{}:{}@/{}?host={}'.format(
    env_value('POSTGRES_USER'),
    env_value('POSTGRES_PASSWORD'),
    env_value('POSTGRES_DB'),
    env_value('POSTGRES_HOST')
))
Base = declarative_base(bind=engine)

Session = sessionmaker(bind=engine)
