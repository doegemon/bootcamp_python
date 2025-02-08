from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select


# The python class will become a table in the database and each instance will represent a row in the table
class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


# Creating the SQLAlchemy engine (object that handles the communication with the database)
engine = create_engine("sqlite:///database.db", echo=True)


def create_db_and_table():
    """
    Function that creates the database (.db) and the table
    """
    SQLModel.metadata.create_all(engine)


def create_heroes():
    """
    Function that inserts values in the table
    """
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parker", age=19)
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        session.commit()


def select_heroes():
    """
    Function that gets all the values in the table
    """
    with Session(engine) as session:
        statement = select(Hero)
        results = session.exec(statement)
        for hero in results:
            print(hero)


def main():
    """
    Function that creates the database and table, insert values in the table and returns all the values from the table.
    """
    create_db_and_table()
    create_heroes()
    select_heroes()


if __name__ == "__main__":
    main()
