import os
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '.env')

load_dotenv(dotenv_path)

DATABASE_URL = os.environ.get('DATABASE_URL')

engine = sqlalchemy.create_engine(DATABASE_URL, echo=True)

Base = sqlalchemy.ext.declarative.declarative_base()

# クラスとしてテーブルを定義する


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

person = Person(name='Mike')
session.add(person)

person2 = Person(name='Nancy')
session.add(person2)
session.commit()

p4 = session.query(Person).filter_by(name='Mike').first()

p4.name = 'Michael'
session.add(p4)
session.commit()

persons = session.query(Person).all()

for person in persons:
    print(person.id, person.name)
