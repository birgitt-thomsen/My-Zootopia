""" Script to update an HTML template with serialized animal data. """

import json

TARGET_HTML = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def extract_skin_types(animals):
    """ Extract skin types from animal data """
    skin_types = []
    for animal in animals:
        if "skin_type" in animal["characteristics"]:
            if animal["characteristics"]["skin_type"] not in skin_types:
                skin_types.append(animal["characteristics"]["skin_type"])
    return skin_types


def get_user_skin_type_input(animals):
    """ Returns the user skin type input """
    while True:
        skin_types = extract_skin_types(animals)
        print(f"\nThe following skin types are available:"
              f"\n{'\n'.join(skin_types)}")
        skin_type_input = input("\nPlease enter the skin type (or press "
                                "Enter to show all): ")
        if skin_type_input.capitalize() in skin_types or skin_type_input == "":
            return skin_type_input
        print(f"\n'{skin_type_input}' is not a valid skin type. Please try again.")


def serialize_animal(animal):
    """ Serializes an animal object """
    output = ''
    output += '<li class="cards__item">'
    output += f"<div class='card__title'>{animal['name']}</div>\n"
    output += '<div class="card__text">'
    output += '<ul class="animal_list">'
    output += (f"<li class='animal_item'><strong>Scientific Name:</strong>"
               f" {animal['taxonomy']['scientific_name']}</li>\n")
    output += (f"<li class='animal_item'><strong>Diet:</strong> "
               f"{animal['characteristics']['diet']}</li>\n")
    output += (f"<li class='animal_item'><strong>Location:</strong> "
               f"{", ".join(animal["locations"])}</li>\n")
    # only set 'type' if it exists
    if "type" in animal["characteristics"]:
        output += (f"<li class='animal_item'><strong>Type:</strong> "
                   f"{animal["characteristics"]["type"]}</li>\n")
    # only set 'color' if it exists
    if "color" in animal["characteristics"]:
        output += (f"<li class='animal_item'><strong>Color:</strong>"
                   f" {animal['characteristics']['color']}</li>\n")
    # only set 'skin_type' if it exists
    if "skin_type" in animal["characteristics"]:
        output += (f"<li class='animal_item'><strong>Skin Type:</strong>"
                   f" {animal['characteristics']['skin_type']}</li>\n")
    output += '</ul>'
    output += '</div>'
    output += '</li>'
    return output


def return_animals_data(animals, skin_type=""):
    """ Returns the animal data """
    output = ""
    for animal in animals:
        if skin_type == "":
            output += serialize_animal(animal)
        elif skin_type.lower() in animal["characteristics"]["skin_type"].lower():
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
    print("\nSuccess! The 'animals.html' file has been updated.")


def main():
    """ Main function that handles the program logic """
    # load animals data
    animals_data = load_data('animals_data.json')

    # load skin types
    skin_type_input = get_user_skin_type_input(animals_data)

    # serialized animal data
    animals_output = return_animals_data(animals_data,skin_type_input)

    # load html template
    html_orig = load_html_template('animals_template.html')

    # replace original html with new animals data
    updated_html = replace_html(html_orig, animals_output)

    # write final output
    write_animals_html('animals.html', updated_html)


if __name__ == "__main__":
    main()
