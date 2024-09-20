# crud.py

from db_connect import session, Recipe, Ingredient
from recipe import Recipe as RecipeClass

# Function to add a new recipe
def add_recipe(name, ingredients, instructions):
    new_recipe = Recipe(name=name, instructions=instructions)
    
    # Add ingredients to the recipe
    for ingredient in ingredients:
        new_ingredient = Ingredient(ingredient_name=ingredient, recipe=new_recipe)
        session.add(new_ingredient)
    
    # Save the recipe and ingredients to the database
    session.add(new_recipe)
    session.commit()
    print(f"Recipe '{name}' added successfully!")

# Function to edit an existing recipe
def edit_recipe(recipe_id, new_name=None, new_ingredients=None, new_instructions=None):
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    
    if not recipe:
        print(f"Recipe with ID {recipe_id} not found.")
        return

    if new_name:
        recipe.name = new_name
    if new_instructions:
        recipe.instructions = new_instructions

    # Clear existing ingredients and add new ones
    if new_ingredients:
        session.query(Ingredient).filter_by(recipe_id=recipe_id).delete()  # Delete old ingredients
        for ingredient in new_ingredients:
            new_ingredient = Ingredient(ingredient_name=ingredient, recipe=recipe)
            session.add(new_ingredient)
    
    session.commit()
    print(f"Recipe '{recipe.name}' updated successfully!")

# Function to delete a recipe
def delete_recipe(recipe_id):
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    
    if not recipe:
        print(f"Recipe with ID {recipe_id} not found.")
        return

    session.delete(recipe)
    session.commit()
    print(f"Recipe '{recipe.name}' deleted successfully!")

# Function to view all recipes
def view_all_recipes():
    recipes = session.query(Recipe).all()
    
    if not recipes:
        print("No recipes found.")
        return
    
    for recipe in recipes:
        print(f"ID: {recipe.id}, Name: {recipe.name}")

# Function to view recipe details
def view_recipe_details(recipe_id):
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    
    if not recipe:
        print(f"Recipe with ID {recipe_id} not found.")
        return
    
    print(f"Recipe Name: {recipe.name}")
    print("Ingredients:")
    for ingredient in recipe.ingredients:
        print(f"- {ingredient.ingredient_name}")
    print(f"Instructions: {recipe.instructions}")

# Function to search for recipes by name
def search_recipe_by_name(name):
    recipes = session.query(Recipe).filter(Recipe.name.like(f"%{name}%")).all()
    
    if not recipes:
        print(f"No recipes found with the name '{name}'.")
        return
    
    for recipe in recipes:
        print(f"ID: {recipe.id}, Name: {recipe.name}")

# Function to suggest recipes based on ingredients
def suggest_recipes(ingredient_list):
    suggested_recipes = session.query(Recipe).join(Ingredient).filter(Ingredient.ingredient_name.in_(ingredient_list)).all()
    
    if not suggested_recipes:
        print("No recipes found matching those ingredients.")
        return
    
    print("Suggested recipes based on ingredients:")
    for recipe in suggested_recipes:
        print(f"ID: {recipe.id}, Name: {recipe.name}")
