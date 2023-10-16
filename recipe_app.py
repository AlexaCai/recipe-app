from sqlalchemy import create_engine
engine = create_engine("mysql://cf-python:password@localhost/task_database")

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "- recipe name: " + self.name + "- recipe difficulty: " + self.difficulty + ">"

    # Method to print a well-formatted version of the recipe
    def __str__(self):
        output = (
            "-" * 10 + "\n" +
            "Recipe id: " + str(self.id) + "\n" +
            "Name of the recipe: " + str(self.name) + "\n" +
            "Cooking time (min): " + str(self.cooking_time) + "\n" +
            "Ingredients: " + str(self.ingredients) + "\n" +
            "Difficulty: " + str(self.difficulty) + "\n" +
            "-" * 10
        )
        return output
    
    def calculate_difficulty(self, cooking_time, ingredients):
        if cooking_time < 10 and len(ingredients) < 4:
            self.difficulty = "easy"
            return self.difficulty
        elif cooking_time < 10 and len(ingredients) >= 4:
            self.difficulty = "medium"
            return self.difficulty
        elif cooking_time >= 10 and len(ingredients) < 4:
            self.difficulty = "intermediate"
            return self.difficulty
        elif cooking_time >= 10 and len(ingredients) >= 4:
            self.difficulty = "hard"
            return self.difficulty

    def return_ingredients_as_list(self):
        if self.ingredients == '':
            return []
        else:
            output = self.ingredients.split(", ")
            return output

# Create the tables of the model defined (class Recipe) above
Base.metadata.create_all(engine)


# First function
def create_recipe():
    try:

        # Creating the recipe name
        name = str(input("Enter the name of the recipe: "))
        name_line = name

        while not name_line.strip() or not name_line.replace(" ", "").isalnum() or len(name_line) > 50:
            if not name_line.strip():
                print("-" * 25)
                print("You must enter a value in this field (cannot stay empty). Please add a recipe name.")
                print("-" * 25)
                name_line = input("Enter the name of the recipe: ")
                name = name_line
            # Ensure the field only contains alpa. characters (with exception for spaces, which are allowed)
            elif not name_line.replace(" ", "").isalnum():
                print("-" * 25)
                print("You must enter an alphanumeric character in this field. Please update your recipe name.")
                print("-" * 25)
                name_line = input("Enter the name of the recipe: ")
                name = name_line
            elif len(name_line) > 50:
                print("-"*25)
                print("A maximum of 50 characters is allowed for a recipe's name. Please reduce the length of your recipe's name.")
                print("-"*25)
                name_line = input("Enter the name of the recipe: ")
                name = name_line

        print("Recipe name added successfully!")


        # Choosing the cooking time in minutes
        cooking_time = input("Enter the cooking time in minutes: ")
        cooking_time_line = cooking_time

        while not cooking_time_line.strip() or cooking_time_line.isnumeric() != True:
            if not cooking_time_line.strip():
                print("-" * 25)
                print("You must enter a value in this field (cannot stay empty). Please add the recipe cooking time in minutes.")
                print("-" * 25)
                cooking_time_line = input("Enter the cooking time in minutes: ")
                cooking_time = cooking_time_line
            elif cooking_time_line.isnumeric() != True:
                print("-"*25)
                print("Only numbers are accepted in this field, please update your entry for a number.")
                print("-"*25)
                cooking_time_line = input("Enter the cooking time in minutes: ")
                cooking_time = cooking_time_line

        print("Recipe cooking time added successfully!")


        # Add the recipe ingredients
        ingredients = []

        number_of_ingredients = input("Enter how many ingredient(s) you would like to add to your recipe: ")

        # First check the number selected by users is ok
        while not number_of_ingredients.strip() or number_of_ingredients.isnumeric() != True:
            if not number_of_ingredients.strip():
                print("-" * 25)
                print("You must enter a value in this field (cannot stay empty). Please add the number of ingredient(s) you want to add for your recipe.")
                print("-" * 25)
                number_of_ingredients = input("Enter how many ingredient(s) you would like to add to your recipe: ")
            elif number_of_ingredients.isnumeric() != True:
                print("-"*25)
                print("Only numbers are accepted in this field, please update your entry for a number.")
                print("-"*25)
                number_of_ingredients = input("Enter how many ingredient(s) you would like to add to your recipe: ")

        for items in range(int(number_of_ingredients)):
                ingredients_input = input("Enter the ingredient (one at a time): ")

                # Second check if the ingredients entered by users are ok
                while not ingredients_input.strip() or not ingredients_input.replace(" ", "").isalnum() or len(ingredients_input) > 255 or ingredients_input in ingredients:
                    if not ingredients_input.strip():
                        print("-" * 25)
                        print("You must enter a value in this field (cannot stay empty). Please add the ingredient name.")
                        print("-" * 25)
                        ingredients_input = input("Enter the ingredient (one at a time): ")
                    # Ensure the field only contains alpa. character (with exception for spaces, which are allowed)
                    elif not ingredients_input.replace(" ", "").isalnum():
                        print("-" * 25)
                        print("You must enter an alphanumeric character in this field. Please update your ingredient name.")
                        print("-" * 25)
                        ingredients_input = input("Enter the ingredient (one at a time): ")
                    elif len(ingredients_input) > 255:
                        print("-----------------------")
                        print("A maximum of 255 characters is allowed for a recipe's ingredient. Please reduce the number of characters of your ingredient that exceed this length.")
                        print("-----------------------")
                        ingredients_input = input("Enter the ingredient (one at a time): ")
                    elif ingredients_input in ingredients:
                        print("-----------------------")
                        print(ingredients_input + " is already in the list, choose another ingredient.")
                        print("-----------------------")
                        ingredients_input = input("Enter the ingredient (one at a time): ")

                if len(ingredients_input) <= 255:
                    if ingredients_input not in ingredients:
                        ingredients.append(ingredients_input)
                        print('Ingredients added to the recipe!')

                ingredients_string = ", ".join(ingredients)
                

        # Calulcate the difficulty based on cooking time and ingredients.
        # By creating an instance of the Recipe class, we can call the calculate_difficulty method on that \
        # instance and set the difficulty attribute specifically for the recipe created by the user. 
        # Recipe_instance is a placeholder that helps calculate/accessing calculate_difficulty function \
        # for a recipe before creating the final recipe object below (recipe_entry).
        recipe_instance = Recipe()
        difficulty = recipe_instance.calculate_difficulty(int(cooking_time), ingredients)

        # Creating a new object from the Recipe model called recipe_entry using the details above
        recipe_entry = Recipe(
            name = name,
            cooking_time = int(cooking_time),
            ingredients = ingredients_string,
            difficulty = difficulty
        )

        print("-"*25)
        print("Here's your newly created recipe:")
        print("Name of the recipe: ", recipe_entry.name)
        print("Cooking time (min): ", recipe_entry.cooking_time)
        print("Ingredients: ", recipe_entry.ingredients)
        print("Difficulty: ", recipe_entry.difficulty)
        print("-"*25)

        # Ensure recipe created is commit / pushed to the database
        session.add(recipe_entry)
        session.commit()

    except:
        print("Something went wrong.")


def view_all_recipes():

    try:
        recipes_list = session.query(Recipe).all()
        if not recipes_list:
            print("There are no recipes in the database, you'll therefore be brought back to the main menu.")
            return None
        else:
            for recipe in recipes_list:
                print(recipe) 
        
        next_action = input("When you want to back to main menu, simply type 'back': ").lower()
        while next_action != 'back':
            next_action = input("Seems like there's a typo. Type 'back' to return to main menu: ").lower()

        if next_action == 'back':
                return None

    except:
        print("Something went wrong.")


def search_by_ingredients():

    try:
        recipes_list = session.query(Recipe).count()
        all_ingredients = []

        if recipes_list == 0:
            print("There are no recipes in the database, you'll therefore be brought back to the main menu.")
            return None
        else:
            results = session.query(Recipe.ingredients).all()
            for items in results:
                ingredient_string = items[0]
                ingredient_list = ingredient_string.split(", ")
                for ingredient in ingredient_list:
                    if ingredient not in all_ingredients:
                        all_ingredients.append(ingredient)
        
        ingredients = sorted(all_ingredients)
        for index, ingredient in enumerate(ingredients, start=1):
            print(str(index) + ". " + ingredient)
            
        # Used to calculate to maximum (or higher) number associated with an ingredient in the list shown \
        # to users. This is later used to ensure users select a number associated with an ingredients that \
        # is within the existing range of numbers displayed on their UI  
        max_index = max(range(1, len(ingredients) + 1))

        print("-----------------------")
        number_picked = input(" Enter the number(s) associated with the ingredient(s) you would like to search for recipes with.\n If you want to search with more than one ingredient, the numbers must be separated by a space an nothing else.\n Your number(s): ")

        while not number_picked.strip() or not number_picked.replace(" ", "").isnumeric() or any(int(num) == 0 for num in number_picked.split()) or any(int(num) > max_index for num in number_picked.split()):
            # Ensure the field is not empty
            if not number_picked.strip():
                print("-" * 25)
                print("You must enter a value in this field (cannot stay empty). Please add the number(s) associated to the ingredient(s) with which you would like to search for recipes. If you want to enter more than one number, make sure to separate them with a space and nothing else.")
                print("-" * 25)
                number_picked = input("Your number(s): ")
            # Ensure only number are added in this field
            elif not number_picked.replace(" ", "").isnumeric():
                print("-"*25)
                print("Only numbers are accepted in this field. Please add the number(s) associated to the ingredient(s) with which you would like to search for recipes with. If you want to enter more than one number, make sure to separate them with a space and nothing else.")
                print("-"*25)
                number_picked = input("Your number(s): ")
            elif any(int(num) == 0 for num in number_picked.split()) or any(int(num) > max_index for num in number_picked.split()):
                print("-"*25)
                print("The number or one of the numbers you entered is not within the range of the available ingredient(s) number(s). You'll be brought back to the main menu. ")
                print("-"*25)
                return None

        ingredients_from_numbers_picked = [int(num) for num in number_picked.split()]
        search_ingredient = [ingredients[num - 1] for num in ingredients_from_numbers_picked]
        print("Selected ingredients:", search_ingredient)

        conditions = []

        for ingredient in search_ingredient:
            print(ingredient)
            like_term = "%" + ingredient + "%"  
            condition = Recipe.ingredients.like(like_term)
            conditions.append(condition) 

        print("-" * 25)
        print("Here are all the recipes containning the ingredients you've searched with. If you want more results, consider reducing the ingredients in your search.")
        related_recipes = session.query(Recipe).filter(*conditions).all()
        print("-----------------------")
        for recipe in related_recipes:
            print(recipe) 

        # To display all recipes containing at least one searched ingredient
        # related_recipes = []

        # for condition in conditions:
        #     recipes = session.query(Recipe).filter(condition).all()
        #     print(recipes)

        # for recipe in related_recipes:
        #     print(recipe)

    except:
        print("Something went wrong.")

def edit_recipe():
    try:
     
        recipes_list = session.query(Recipe).all()

        if not recipes_list:
            print("There are no recipes in the database, you'll therefore be brought back to the main menu.")
            return None
        
        else:
            results = []

            # Extract the ID and name of each recipe, and stored this in results variables
            for recipe in recipes_list:
                recipe_id = recipe.id
                recipe_name = recipe.name
                results.append((recipe_id, recipe_name))
            
            # Retrieve each recipe from the database based on the recipes' id stored in the results variable \
            # All avaialble recipe are displayed to users
            for recipe in results:
                recipe_id = recipe[0]  
                related_recipes = session.query(Recipe).filter(Recipe.id == recipe_id).all()
                for recipe in related_recipes:
                    print(recipe) 

            # Used to calculate to maximum (or higher) id associated with recipe in the list shown to users \
            # This is later used to ensure users select an id associated with a recipe that is within the \
            # the existing range of id displayed on their UI  
            highest_id = max(recipe[0] for recipe in results)

        print("-----------------------")
        recipe_id_picked = input(" Enter the id number associated with the recipe you would like to update: ")

        while not recipe_id_picked.strip() or recipe_id_picked.isnumeric() != True or int(recipe_id_picked) == 0 or int(recipe_id_picked) > highest_id:
            # Ensure the field is not empty
            if not recipe_id_picked.strip():
                print("-" * 25)
                print("You must enter a value in this field (cannot stay empty). Please add the id number associated with the recipe you would like to update.")
                print("-" * 25)
                recipe_id_picked = input("Your number(s): ")
            # Ensure only number are added in this field
            elif recipe_id_picked.isnumeric() != True:
                print("-"*25)
                print("Only numbers are accepted in this field. Please add the id number associated with the recipe you would like to update.")
                print("-"*25)
                recipe_id_picked = input("Your number(s): ")
            elif int(recipe_id_picked) == 0 or int(recipe_id_picked) > highest_id:
                print("-"*25)
                print("The number you entered is not within the range of the available id number(s). You'll be brought back to the main menu. ")
                print("-"*25)
                return None

        # Retrieve from the database the recipe to be updated based on the recipe id picked by users
        recipe_to_edit = session.query(Recipe).get(int(recipe_id_picked))
        print("-"*25)
        print("Fields that can be updated:")
        print("1. Name of the recipe: ", recipe_to_edit.name)
        print("2. Cooking time (min): ", recipe_to_edit.cooking_time)
        print("3. Ingredients: ", recipe_to_edit.ingredients)
        print("-"*25)

        edit_number_chosen = input("Enter the number associated with the field you would like to update: ")

        while not edit_number_chosen.strip() or edit_number_chosen.isnumeric() != True or not 0 < int(edit_number_chosen) <= 3:
            # Ensure the field is not empty
            if not edit_number_chosen.strip():
                print("-" * 25)
                print("You must enter a value in this field (cannot stay empty). Please add the number associated with the field you would like to update.")
                print("-" * 25)
                edit_number_chosen = input("Your number: ")
            # Ensure only number are added in this field
            elif edit_number_chosen.isnumeric() != True:
                print("-"*25)
                print("Only numbers are accepted in this field. Please add the number associated with the field you would like to update.")
                print("-"*25)
                edit_number_chosen = input("Your number: ")
            elif not 0 < int(edit_number_chosen) <= 3:
                print("-"*25)
                print("The number you entered is not within the range of the available number. Please pick a number from 1 to 3. ")
                print("-"*25)
                edit_number_chosen = input("Your number: ")

        if int(edit_number_chosen) == 1:
                updated_name = input("Enter the new/updated name for the recipe: ")

                while not updated_name.strip() or not updated_name.replace(" ", "").isalnum() or len(updated_name) > 50:
                    if not updated_name.strip():
                        print("-" * 25)
                        print("You must enter a value in this field (cannot stay empty). Please add a recipe name.")
                        print("-" * 25)
                        updated_name = input("Enter the new/updated name for the recipe: ")
                    # Ensure the field only contains alpa. characters (with exception for spaces, which are allowed)
                    elif not updated_name.replace(" ", "").isalnum():
                        print("-" * 25)
                        print("You must enter an alphanumeric character in this field. Please update your recipe name.")
                        print("-" * 25)
                        updated_name = input("Enter the new/updated name for the recipe: ")
                    # Ensure the recipe name is 50 or less characters
                    elif len(updated_name) > 50:
                        print("-"*25)
                        print("A maximum of 50 characters is allowed for a recipe's name. Please reduce the length of your recipe's name.")
                        print("-"*25)
                        updated_name = input("Enter the new/updated name for the recipe: ")

                print("Recipe name " + updated_name + " updated successfully!")

                recipe_to_edit.name = updated_name
                print("-"*25)
                print("Here's your newly updated recipe.")
                print(recipe_to_edit)

                # Commit the change in the database
                session.add(recipe_to_edit)
                session.commit()

                # Ask user what that wanna do next
                next_action = input("What would you like to do next?\n1. Go back to editing recipes\n2. Return to the main menu\nEnter the number associated with your choice: ")
                while next_action not in ['1', '2']:
                    print('Your answer must be 1 or 2, please enter a correct input')
                    next_action = input("What would you like to do next?\n1. Go back to editing recipes\n2. Return to the main menu\nEnter the number associated with your choice: ")

                if next_action == '1':
                    edit_recipe()  
                elif next_action == '2':
                    return  


        elif int(edit_number_chosen) == 2:
                updated_cooking_time = input("Enter the new/updated cooking time for the recipe: ")

                while not updated_cooking_time.strip() or updated_cooking_time.isnumeric() != True:
                    # Ensure the field is not empty
                    if not updated_cooking_time.strip():
                        print("-" * 25)
                        print("You must enter a value in this field (cannot stay empty). Please add the recipe cooking time in minutes.")
                        print("-" * 25)
                        updated_cooking_time = input("Enter the new/updated cooking time for the recipe: ")
                    # Ensure only number are added in this field
                    elif updated_cooking_time.isnumeric() != True:
                        print("-"*25)
                        print("Only numbers are accepted in this field, please update your entry for a number.")
                        print("-"*25)
                        updated_cooking_time = input("Enter the new/updated cooking time for the recipe: ")

                recipe_to_edit.cooking_time = int(updated_cooking_time)
                print("Recipe cooking time " + str(updated_cooking_time) + " min updated successfully!")

                # From the recipe within recipe_to_edit, retrieve the updated cooking time and the ingredients to \
                # pass them as argument in calculate_difficulty to recalculte recipe difficulty level that might \
                # have change depending on the new cooking time.

                # Note: return_ingredients_as_list() in recipe_to_edit.return_ingredients_as_list() is a method \
                # defined in the Recipe class at the beginning of the file, which allow to return the list of \
                # ingredients from a string.
                updated_difficulty = recipe_to_edit.calculate_difficulty(recipe_to_edit.cooking_time, recipe_to_edit.return_ingredients_as_list())
                recipe_to_edit.difficulty = updated_difficulty

                print("-"*25)
                print("Here's your newly updated recipe:")
                print(recipe_to_edit)

                # Commit the change in the database
                session.add(recipe_to_edit)
                session.commit()

                # Ask user what that wanna do next
                next_action = input("What would you like to do next?\n1. Go back to editing recipes\n2. Return to the main menu\nEnter the number associated with your choice: ")
                while next_action not in ['1', '2']:
                    print('Your answer must be 1 or 2, please enter a correct input')
                    next_action = input("What would you like to do next?\n1. Go back to editing recipes\n2. Return to the main menu\nEnter the number associated with your choice: ")

                if next_action == '1':
                    edit_recipe()  
                elif next_action == '2':
                    return  


        elif int(edit_number_chosen) == 3:
                print("-"*25)
                print("What would you like to do?")
                print("1. Remove existing ingredient(s) ")
                print("2. Add a new ingredients to the existing ingredients ")
                print("3. Replace the whole list of ingredients with a new list. ")
                print("-"*25)
                edit_number_chosen = input("Enter the number associated with the field you would like to update: ")

                while not edit_number_chosen.strip() or edit_number_chosen.isnumeric() != True or not 0 < int(edit_number_chosen) <= 3:
                # Ensure the field is not empty
                    if not edit_number_chosen.strip():
                        print("-" * 25)
                        print("You must enter a value in this field (cannot stay empty). Please add the number associated with the field you would like to update.")
                        print("-" * 25)
                        edit_number_chosen = input("Your number: ")
                    # Ensure only number are added in this field
                    elif edit_number_chosen.isnumeric() != True:
                        print("-"*25)
                        print("Only numbers are accepted in this field. Please add the number associated with the field you would like to update.")
                        print("-"*25)
                        edit_number_chosen = input("Your number: ")
                    elif not 0 < int(edit_number_chosen) <= 3:
                        print("-"*25)
                        print("The number you entered is not within the range of the available number. Please pick a number from 1 to 3. ")
                        print("-"*25)
                        edit_number_chosen = input("Your number: ")

                while True:
                    if int(edit_number_chosen) == 1:
                            if recipe_to_edit.ingredients == '':
                                print("There's no ingredients to remove. You'll be brought back to the main recipes update view.")
                                edit_recipe()
                            else:
                                # Show to users all ingredients that can be removed
                                print("-"*25)
                                print("Here are the recipe' ingredients")
                                ingredients_list = recipe_to_edit.return_ingredients_as_list()
                                ingredient = sorted(recipe_to_edit.ingredients)
                                for index, ingredient in enumerate(recipe_to_edit.return_ingredients_as_list(), start=1):
                                    print(str(index) + ". " + ingredient)
                                ingredient_number_to_remove = input("Enter the number associated with the ingreidient you would like to remove: ")

                                # Remove the ingredient picked by users
                                removed_ingredient = ingredients_list.pop(int(ingredient_number_to_remove) - 1)
                                recipe_to_edit.ingredients = ", ".join(ingredients_list)  # Update the ingredients string
                                print(removed_ingredient + ' has been deleted.')

                                # Update the difficulty level if necessary based on the ingredients changes
                                updated_difficulty = recipe_to_edit.calculate_difficulty(recipe_to_edit.cooking_time, recipe_to_edit.return_ingredients_as_list())
                                recipe_to_edit.difficulty = updated_difficulty
                                print(recipe_to_edit)

                                # session.add(recipe_entry)
                                # session.commit()

                                # Ask the user what he wants to do now
                                another_action = input("Do you want to remove another ingredient? Enter yes or no: ").lower()                        
                                while another_action not in ['yes', 'no']:
                                    print('Your answer must be yes or no, please enter a correct input')
                                    another_action = input("Do you want to remove another ingredient? Enter yes or no: ")

                                if another_action == 'yes':
                                    continue
                                elif another_action == 'no':
                                        print('print somehting')
                                        next_action = input("What would you like to do next?\n1. Go back to editing recipes\n2. Return to the main menu\nEnter the number associated with your choice: ")

                                        while next_action not in ['1', '2']:
                                            print('Your answer must be 1 or 2, please enter a correct input')
                                            next_action = input("What would you like to do next?\n1. Go back to editing recipes\n2. Return to the main menu\nEnter the number associated with your choice: ")

                                        if next_action == '1':
                                            edit_recipe()
                                        elif next_action == '2':
                                            return

                    if int(edit_number_chosen) == 2:
                            if recipe_to_edit.ingredients == '':
                                print("There's no ingredients to remove. You'll be brought back to the main recipes update view.")
                                edit_recipe()
                            else:
                                # Show to users all ingredients that can be removed
                                print("-"*25)
                                print("Here are the recipe' ingredients")
                                ingredients_list = recipe_to_edit.return_ingredients_as_list()
                                ingredient = sorted(recipe_to_edit.ingredients)
                                for index, ingredient in enumerate(recipe_to_edit.return_ingredients_as_list(), start=1):
                                    print(str(index) + ". " + ingredient)
                                added_ingredient = input("Enter the ingredient you would like to add: ")

                                ingredients_list.append(added_ingredient)
                                recipe_to_edit.ingredients = ", ".join(ingredients_list)  # Update the ingredients string
                                print(added_ingredient + ' has been added.')

                                # Update the difficulty level if necessary based on the ingredients changes
                                updated_difficulty = recipe_to_edit.calculate_difficulty(recipe_to_edit.cooking_time, recipe_to_edit.return_ingredients_as_list())
                                recipe_to_edit.difficulty = updated_difficulty
                                print(recipe_to_edit)

                                session.add(recipe_to_edit)
                                session.commit()

                                # Ask the user what he wants to do now
                                another_action = input("Do you want to add another ingredient? Enter yes or no: ").lower()                        
                                while another_action not in ['yes', 'no']:
                                    print('Your answer must be yes or no, please enter a correct input')
                                    another_action = input("Do you want to add another ingredient? Enter yes or no: ")

                                if another_action == 'yes':
                                    continue
                                elif another_action == 'no':
                                        print('print somehting')
                                        next_action = input("What would you like to do next?\n1. Go back to editing recipes\n2. Return to the main menu\nEnter the number associated with your choice: ")

                                        while next_action not in ['1', '2']:
                                            print('Your answer must be 1 or 2, please enter a correct input')
                                            next_action = input("What would you like to do next?\n1. Go back to editing recipes\n2. Return to the main menu\nEnter the number associated with your choice: ")

                                        if next_action == '1':
                                            edit_recipe()
                                        elif next_action == '2':
                                            return
    except:
        print("Something went wrong.")

def delete_recipe():
    try:
     
        recipes_list = session.query(Recipe).all()

        if not recipes_list:
            print("There are no recipes in the database, you'll therefore be brought back to the main menu.")
            return None
        
        else:

            results = []

            # Extract the ID and name of each recipe, and stored this in results variables
            for recipe in recipes_list:
                recipe_id = recipe.id
                recipe_name = recipe.name
                results.append((recipe_id, recipe_name))
            
            # Retrieve each recipe from the database based on the recipes' id stored in the results variable \
            # All avaialble recipe are displayed to users
            for recipe in results:
                recipe_id = recipe[0]  
                related_recipes = session.query(Recipe).filter(Recipe.id == recipe_id).all()
                for recipe in related_recipes:
                    print(recipe) 

            # Used to calculate to maximum (or higher) id associated with recipe in the list shown to users \
            # This is later used to ensure users select an id associated with a recipe that is within the \
            # the existing range of id displayed on their UI  
            existing_recipe_ids = [recipe.id for recipe in session.query(Recipe.id).all()]

            print("-----------------------")
            recipe_id_picked = input(" Enter the id number associated with the recipe you would like to delete: ")

            while not recipe_id_picked.strip() or recipe_id_picked.isnumeric() != True or int(recipe_id_picked) not in existing_recipe_ids:
                # Ensure the field is not empty
                if not recipe_id_picked.strip():
                    print("-" * 25)
                    print("You must enter a value in this field (cannot stay empty). Please add the id number associated with the recipe you would like to delete.")
                    print("-" * 25)
                    recipe_id_picked = input("Your number(s): ")
                # Ensure only number are added in this field
                elif recipe_id_picked.isnumeric() != True:
                    print("-"*25)
                    print("Only numbers are accepted in this field. Please add the id number associated with the recipe you would like to delete.")
                    print("-"*25)
                    recipe_id_picked = input("Your number(s): ")
                elif int(recipe_id_picked) not in existing_recipe_ids:
                    print("-"*25)
                    print("The number you entered is not associated with a recipe id number. You'll be brought back to the main menu. ")
                    print("-"*25)
                    return None

            # Retrieve from the database the recipe to be delete based on the recipe id picked by users
            recipe_to_be_deleted = session.query(Recipe).get(int(recipe_id_picked))
            print("-"*25)
            print("Here's the recipe you are about to delete:")
            print(recipe_to_be_deleted)

            delete_confirmation = input("Are you sure you want to delete this recipe? Enter yes or no: ").lower()                        
            while delete_confirmation not in ['yes', 'no']:
                print('Your answer must be yes or no, please enter a correct input')
                delete_confirmation = input("Are you sure you want to delete this recipe? Enter yes or no: ").lower()                        

            if delete_confirmation == 'yes':
                    recipe_to_be_deleted = session.query(Recipe).filter(Recipe.id == recipe_id_picked).one()
                    session.delete(recipe_to_be_deleted)                    
                    session.commit()
                    print('Your recipe has been deleted successfully!')
                    
                    next_action = input("What would you like to do next?\n1. Go back to editing recipes\n2. Return to the main menu\nEnter the number associated with your choice: ")

                    while next_action not in ['1', '2']:
                        print('Your answer must be 1 or 2, please enter a correct input')
                        next_action = input("What would you like to do next?\n1. Go back to editing recipes\n2. Return to the main menu\nEnter the number associated with your choice: ")

                    if next_action == '1':
                        edit_recipe()
                    elif next_action == '2':
                        return
                
            elif delete_confirmation == 'no':
                    next_action = input("What would you like to do next?\n1. Go back to editing recipes\n2. Return to the main menu\nEnter the number associated with your choice: ")

                    while next_action not in ['1', '2']:
                        print('Your answer must be 1 or 2, please enter a correct input')
                        next_action = input("What would you like to do next?\n1. Go back to editing recipes\n2. Return to the main menu\nEnter the number associated with your choice: ")

                    if next_action == '1':
                        edit_recipe()
                    elif next_action == '2':
                        return

    except:
        print("Something went wrong.")

def main_menu():
    user_choice = None

    while user_choice != "quit":
        print("Main menu")
        print("-----------------------")
        print("Pick a choice")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for a recipe by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print('Type "quit" to exit')
        user_choice = input('Your choice (pick a number or type "quit"): ')

        if user_choice == "1":
            create_recipe()
            continue
        elif user_choice == "2":
            view_all_recipes()
            continue
        elif user_choice == "3":
            search_by_ingredients
            continue
        elif user_choice == "4":
            edit_recipe
            continue
        elif user_choice == "5":
            delete_recipe()
            continue
        elif user_choice.lower() == "quit":
            # session.close()
            # engine.dispose()
            break
        else:
            print('Wrong input, please pick a number or type "quit": ')
            continue

main_menu()