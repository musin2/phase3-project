# Recipe Manager CLI Project

This is a simple **Command Line Interface (CLI)** application that helps users manage recipes. The project is written in **Python** using **SQLAlchemy** for database management and follows an **Object-Oriented Programming (OOP)** structure. It allows users to add, edit, delete, and view recipes, as well as suggest recipes based on ingredients.

## Features

1. **Add a new recipe**
2. **Edit an existing recipe**
3. **Delete a recipe**
4. **View all recipes**
5. **View recipe details**
6. **Search recipes by name**
7. **Suggest recipes based on ingredients**
8. **Menu navigation**

## Requirements

- Python 3.10+
- SQLAlchemy

You can install the required packages by running:

```bash
    pipenv install
```

## How to Run

1. Clone or download the project.
2. Navigate to the project directory.
3. Activate the virtual environment and run the program:

```bash
pipenv shell
python3 main.py
```

Follow the prompts in the CLI menu to manage your recipes!

## How the Database Works

The application uses SQLite as the database, and the data is stored in a local file called _recipe_manager.db_. SQLAlchemy is used to handle interactions with the database, and the following tables are created:

- **Recipes**: Stores the recipe ID, name, and instructions.
- **Ingredients**: Stores the ingredient names and links them to the corresponding recipe via a foreign key.
