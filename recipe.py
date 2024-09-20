class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients  # List of ingredient names
        self.instructions = instructions

    #Display recipe details
    def display_recipe(self):
        print(f"Recipe Name: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print(f"Instructions: {self.instructions}")
    
    #Edit recipe details
    def edit_recipe(self, new_name=None, new_ingredients=None, new_instructions=None):
        if new_name:
            self.name = new_name
        if new_ingredients:
            self.ingredients = new_ingredients
        if new_instructions:
            self.instructions = new_instructions
