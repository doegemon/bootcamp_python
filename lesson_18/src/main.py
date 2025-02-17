import time
import random
from controller import catch_pokemon_data, add_pokemon_to_db


def main():
    while True:
        pokemon_id = random.randint(1, 350)
        pokemon_schema = catch_pokemon_data(pokemon_id)
        if pokemon_schema:
            print(f"Adding {pokemon_schema.name} to the database.")
            add_pokemon_to_db(pokemon_schema)
        else:
            print(f"It wasn't possible to get data from the Pokemon ID {pokemon_id}.")
        time.sleep(10)


if __name__ == "__main__":
    main()
