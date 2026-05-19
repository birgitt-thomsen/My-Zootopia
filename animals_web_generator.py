import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf8") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

def get_animal_data(animals):
    output = ""
    for animal in animals:
        output += '<li class="cards__item">'
        output += f"<div class='card__title'>{animal['name']}</div>\n"
        output += '<p class="card__text">'
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
        output += f"<strong>Location:</strong> {", ".join(animal["locations"])}<br/>\n"
        # only set 'type' if it exists
        if "type" in animal["characteristics"]:
            output += f"<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n"
        output += '</p>'
        output += '</li>'
    return output

animals_output = get_animal_data(animals_data)


with open("animals_template.html", "r", encoding="utf8") as file:
    html = file.read()


new_html = html.replace("__REPLACE_ANIMALS_INFO__", animals_output)

with open("animals.html", "w", encoding="utf8") as file:
    file.write(new_html)