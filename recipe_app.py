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
            "Recipe added successfully! " + "\n" +
            "Name of the recipe: " + str(self.name) + "\n" +
            "Cooking time (min): " + str(self.cooking_time) + "\n" +
            "Ingredients: " + str(self.ingredients) + "\n" +
            "Difficulty: " + str(self.difficulty) + "\n" +
            "-" * 10
        )
        return output
    
    # Method to calculate difficulty of a recipe
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

def create_recipe():
    try:

        #Name the recipe
        name = str(input("Enter the name of the recipe: "))
        name_line = name

        while not name_line.strip() or not name_line.replace(" ", "").isalnum() or len(name_line) > 50:
            if not name_line.strip():
                print("-" * 25)
                print("You must enter a value in this field (cannot stay empty). Please add a recipe name.")
                print("-" * 25)
                name_line = input("Enter the name of the recipe: ")
                name = name_line
            # Ensure the field only contains alpa. character (with exception for spaces, which are allowed)
            elif not name_line.replace(" ", "").isalnum():
                print("-" * 25)
                print("You must enter an alphanumeric character in this field. Please update your recipe name.")
                print("-" * 25)
                name_line = input("Enter the name of the recipe: ")
                name = name_line
            # Ensure the recipe name is 50 or less characters
            elif len(name_line) > 50:
                print("-"*25)
                print("A maximum of 50 characters is allowed for a recipe's name. Please reduce the length of your recipe's name.")
                print("-"*25)
                name_line = input("Enter the name of the recipe: ")
                name = name_line

        #Choosing the cooking time in minutes
        cooking_time = input("Enter the cooking time in minutes: ")
        cooking_time_line = cooking_time

        while not cooking_time_line.strip() or cooking_time_line.isnumeric() != True:
            # Ensure the field is not empty
            if not cooking_time_line.strip():
                print("-" * 25)
                print("You must enter a value in this field (cannot stay empty). Please add the recipe cooking time in minutes.")
                print("-" * 25)
                cooking_time_line = input("Enter the cooking time in minutes: ")
                cooking_time = cooking_time_line
            # Ensure only number are added in this field
            elif cooking_time_line.isnumeric() != True:
                print("-"*25)
                print("Only numbers are accepted in this field, please update your entry for a number.")
                print("-"*25)
                cooking_time_line = input("Enter the cooking time in minutes: ")
                cooking_time = cooking_time_line


        #Add the ingredients
        ingredients = []

        number_of_ingredients = input("Enter how many ingredient(s) you would like to add to your recipe: ")

        while not number_of_ingredients.strip() or number_of_ingredients.isnumeric() != True:
            # Ensure the field is not empty
            if not number_of_ingredients.strip():
                print("-" * 25)
                print("You must enter a value in this field (cannot stay empty). Please add the number of ingredient(s) you want to add for your recipe.")
                print("-" * 25)
                number_of_ingredients = input("Enter how many ingredient(s) you would like to add to your recipe: ")
            # Ensure only number are added in this field
            elif number_of_ingredients.isnumeric() != True:
                print("-"*25)
                print("Only numbers are accepted in this field, please update your entry for a number.")
                print("-"*25)
                number_of_ingredients = input("Enter how many ingredient(s) you would like to add to your recipe: ")

        for items in range(int(number_of_ingredients)):
                ingredients_input = input("Enter the ingredient: ")

                while not ingredients_input.strip() or not ingredients_input.replace(" ", "").isalnum() or len(ingredients_input) > 50 or ingredients_input in ingredients:
                    # Ensure the field is not empty
                    if not ingredients_input.strip():
                        print("-" * 25)
                        print("You must enter a value in this field (cannot stay empty). Please add the ingredient name.")
                        print("-" * 25)
                        ingredients_input = input("Enter the name of the recipe: ")
                    # Ensure the field only contains alpa. character (with exception for spaces, which are allowed)
                    elif not ingredients_input.replace(" ", "").isalnum():
                        print("-" * 25)
                        print("You must enter an alphanumeric character in this field. Please update your ingredient name.")
                        print("-" * 25)
                        ingredients_input = input("Enter the name of the recipe: ")
                    # Ensure the ingredient name is 255 or less characters
                    elif len(ingredients_input) > 255:
                        print("-----------------------")
                        print("A maximum of 255 characters is allowed for a recipe's ingredient. Please reduce the number of characters of your ingredient that exceed this length.")
                        print("-----------------------")
                        ingredients_input = input("Enter the name of the recipe: ")
                    elif ingredients_input in ingredients:
                        print("-----------------------")
                        print(ingredients_input + " is already in the list, choose another ingredient.")
                        print("-----------------------")
                        ingredients_input = input("Enter the name of the recipe: ")

                if len(ingredients_input) <= 255:
                    if ingredients_input not in ingredients:
                        ingredients.append(ingredients_input)
                        print('Ingredients added to the recipe!')

                ingredients_string = ", ".join(ingredients)
                

        #Calulcate the difficulty based on cooking time and ingredients
        # By creating an instance of the Recipe class, we can call the calculate_difficulty method on that \
        # instance and set the difficulty attribute specifically for the recipe created by the user. 
        # Recipe_instance is a placeholder that helps calculate/accessing calculate_difficulty function \
        # for a recipe before creating the final recipe object below (recipe_entry).
        recipe_instance = Recipe()
        difficulty = recipe_instance.calculate_difficulty(int(cooking_time), ingredients)

        #### Creating a new object from the Recipe model called recipe_entry using the details above
        recipe_entry = Recipe(
            name = name,
            cooking_time = int(cooking_time),
            ingredients = ingredients_string,
            difficulty = difficulty
        )

        print(recipe_entry)

        session.add(recipe_entry)
        session.commit()

    except:
        print("Something went wrong.")




create_recipe()