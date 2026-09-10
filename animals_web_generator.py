import data_fetcher

# Program flow:
# data_fetcher.fetch_data()     → API → Python data
# get_animal_info()             → extract relevant animal data
# display_animal()              → Python data → terminal (optional)
# serialize_animal()            → Python data → HTML string
# load_template()               → HTML file → string
# save_html()                   → string → HTML file
# main()                        → coordinates data fetching and HTML generation


def get_animal_info(animal):
    """Return selected animal data as a dictionary."""

    characteristics = animal.get("characteristics", {})

    return {
        "name": animal.get("name"),
        "diet": characteristics.get("diet"),
        "locations": animal.get("locations", []),
        "type": characteristics.get("type"),
    }


def display_animal(animal):
    """Display selected information for one animal."""

    animal_info = get_animal_info(animal)

    if animal_info["name"]:
        print(f"Name: {animal_info['name']}")

    if animal_info["diet"]:
        print(f"Diet: {animal_info['diet']}")

    if animal_info["locations"]:
        print(f"Location: {', '.join(animal_info['locations'])}")

    if animal_info["type"]:
        print(f"Type: {animal_info['type']}")

    print()


def serialize_animal(animal):
    """Return an HTML string containing a card for one animal."""

    animal_info = get_animal_info(animal)

    animal_html = '<li class="cards__item">\n'

    if animal_info["name"]:
        animal_html += (
            f'<div class="card__title">{animal_info["name"]}</div>\n'
        )

    animal_html += '<div class="card__text">\n'
    animal_html += '<ul class="card__details">\n'

    if animal_info["diet"]:
        animal_html += (
            f'<li class="card__detail">'
            f'<strong>Diet:</strong> {animal_info["diet"]}</li>\n'
        )

    if animal_info["locations"]:
        animal_html += (
            f'<li class="card__detail">'
            f'<strong>Location:</strong> '
            f'{", ".join(animal_info["locations"])}</li>\n'
        )

    if animal_info["type"]:
        animal_html += (
            f'<li class="card__detail">'
            f'<strong>Type:</strong> {animal_info["type"]}</li>\n'
        )

    animal_html += '</ul>\n'
    animal_html += '</div>\n'
    animal_html += '</li>\n'

    return animal_html


def load_template(file_path):
    """Read and return the contents of an HTML file."""

    with open(file_path, "r", encoding="utf-8") as fileobj:
        return fileobj.read()


def save_html(file_path, html_content):
    """Write HTML content to a file."""

    with open(file_path, "w", encoding="utf-8") as fileobj:
        fileobj.write(html_content)


def main():
    """Load animal data and generate the HTML page."""

    animal_name = input("Enter an animal name: ")

    animals_data = data_fetcher.fetch_data(animal_name)

    all_animals_html = ""

    if animals_data:
        for animal in animals_data:
            all_animals_html += serialize_animal(animal)
    else:
        all_animals_html = (
            f'<h2>The animal "{animal_name}" is not in the database.</h2>'
        )

    animals_template = load_template("animals_template.html")

    # Replace the placeholder and its existing indentation
    # with generated animal cards.
    animals_html = animals_template.replace(
        "            __REPLACE_ANIMALS_INFO__",
        all_animals_html
    )

    save_html("animals.html", animals_html)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
