""" Script to update an html template with serialized animal data. """

import json

TARGET_HTML = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """ Serializes an animal object """
    output = ''
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


def return_animals_data(animals):
    """ Returns the animal data """
    output = ""
    for animal in animals:
        output += serialize_animal(animal)
    return output


def load_html_template(file_path):
    """ Loads an HTML file """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def replace_html(html, animals):
    """ Replaces the HTML template with new animals data """
    return html.replace(TARGET_HTML, animals)



def write_animals_html(file_path, html):
    """ Writes the animal data into an HTML file """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html)


def main():
    """ Main function """
    # load animals data
    animals_data = load_data('animals_data.json')

    # serialized animal data
    animals_output = return_animals_data(animals_data)

    # load html template
    html_orig = load_html_template('animals_template.html')

    # replace original html with new animals data
    updated_html = replace_html(html_orig, animals_output)

    # write final output
    write_animals_html('animals.html', updated_html)


if __name__ == "__main__":
    main()
