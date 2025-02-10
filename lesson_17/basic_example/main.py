from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Creating Database and Table
engine = create_engine("sqlite:///mydatabase.db", echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)

# Creating a session to add value to the Table
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="John", age=27)
session.add(new_user)
session.commit()

# Getting data from the Table
user = session.query(User).filter_by(name="John").first()
print(f"User found: {user.name}, age: {user.age}")
