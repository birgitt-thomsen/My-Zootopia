import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf8") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

def print_animal_data(animals):
    for animal in animals:
        name = animal["name"]
        # only set 'diet' if it exists
        if "diet" in animal["characteristics"]:
            diet = animal["characteristics"]["diet"]
        # only set 'location' if it exists
        if animal["locations"]:
            location = ", ".join(animal["locations"])
        # only set 'type' if it exists
        if "type" in animal["characteristics"]:
            type = animal["characteristics"]["type"]

        print("Name:", name)
        print("Diet:", diet)
        print("Location:", location)
        print("Type:", type)
        print()

print_animal_data(animals_data)