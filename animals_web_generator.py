import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf8") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

def get_animal_data(animals):
    output = ""
    for animal in animals:
        output += f"Name: {animal['name']}\n"
        output += f"Diet: {animal['characteristics']['diet']}\n"
        output += f"Location: {", ".join(animal["locations"])}\n"
        # only set 'type' if it exists
        if "type" in animal["characteristics"]:
            output += f"Type: {animal["characteristics"]["type"]}\n"
        output += "\n"
    return output

animals_output = get_animal_data(animals_data)


with open("animals_template.html", "r", encoding="utf8") as file:
    html = file.read()


new_html = html.replace("__REPLACE_ANIMALS_INFO__", animals_output)

with open("animals.html", "w", encoding="utf8") as file:
    file.write(new_html)