# Zootopia with API 🦁

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![API](https://img.shields.io/badge/API-Ninjas-orange)
![License](https://img.shields.io/badge/License-MIT-green)

Zootopia with API is a small Python application that fetches animal information from the **API Ninjas Animals API** and generates an HTML webpage displaying the results.

The application asks the user to enter an animal name, retrieves the corresponding information from the API, and generates an `animals.html` webpage using an HTML template.

## Features

* Search for an animal by name
* Display the animal's diet, location, and type
* Generate an `animals.html` webpage from an HTML template
* Show a message when no animal is found
* Keep the API key secure using environment variables

## Requirements

* **Python 3**
* `requests`
* `python-dotenv`
* An **API Ninjas API key**

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add your API key:

```text
API_KEY=your_api_key_here
```

The `.env` file is excluded from Git using `.gitignore` so that the API key is not committed to the repository.

## Usage

Run the application with:

```bash
python animals_web_generator.py
```

Enter the name of an animal when prompted:

```text
Enter an animal name: fox
```

The application fetches the animal data and generates an `animals.html` file.

Open `animals.html` in a web browser to view the generated webpage.

## Project Structure

```text
Zootopia-with-API/
├── animals_template.html
├── animals_web_generator.py
├── data_fetcher.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies

* Python
* Requests
* python-dotenv
* HTML/CSS
* API Ninjas Animals API

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
