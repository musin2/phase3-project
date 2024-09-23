from crud import (
    add_recipe,
    edit_recipe,
    delete_recipe,
    view_all_recipes,
    view_recipe_details,
    search_recipe_by_name,
    suggest_recipes,
)


def main_menu():
    while True:
        print("\nRecipe Manager CLI")
        print("1. Add a new recipe")
        print("2. Edit an existing recipe")
        print("3. Delete a recipe")
        print("4. View all recipes")
        print("5. View recipe details")
        print("6. Search recipes by name")
        print("7. Suggest recipes based on ingredients")
        print("8. Exit")

        choice = input("\nChoose an option: ")

        match choice:
            case "1":
                # Add new recipe
                name = input("Enter recipe name: ")
                # recipe name validation
                if not name:
                    print("Recipe name cannot be empty!!!")
                    continue
                if len(name) > 150:  #length limit
                    print("Recipe name is too long. Maximum length is 150 characters.")
                    continue
                
                ingredients = input("Enter ingredients (comma separated): ").split(",")
                #Ingredients validation - all() -> returns true if all items in an iterable are true
                if not ingredients or all(ingredient.strip() == "" for ingredient in ingredients):
                    print("Ingredients cannot be empty!!!")
                    continue

                instructions = input("Enter instructions: ")
                #Validate instructions
                if not instructions:
                    print("Instructions cannot be empty!!!")
                    continue
                
                add_recipe(name, ingredients, instructions)

            case "2":
                # Edit existing recipe
                recipe_id = int(input("Enter recipe ID to edit: "))
                edit_recipe(recipe_id)

            case "3":
                # Delete a recipe
                recipe_id = int(input("Enter recipe ID to delete: "))
                delete_recipe(recipe_id)

            case "4":
                # View all recipes
                view_all_recipes()

            case "5":
                # View recipe details
                recipe_id = int(input("Enter recipe ID to view details: "))
                view_recipe_details(recipe_id)

            case "6":
                # Search recipe by name
                name = input("Enter the recipe name to search for: ")
                search_recipe_by_name(name)

            case "7":
                # Suggest recipes based on ingredients
                ingredients = (
                    input("Enter ingredients (comma separated): ").lower().split(",")
                )
                suggest_recipes(ingredients)

            case "8":
                # Exit the program
                print("Exiting Recipe Manager. Goodbye!")
                break

            case _:
                print("Invalid option. Please try again.")


main_menu()
