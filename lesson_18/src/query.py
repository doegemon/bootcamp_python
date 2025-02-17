from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from models import Pokemon

engine = create_engine("sqlite:///../pokemon.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# Getting data from the Table
result = session.query(Pokemon.name, Pokemon.type).all()

for name, type in result:
    print(f"Pokemon: {name} | Types: {type}")
