# Create a database / table and establish connection

import mysql.connector

conn = mysql.connector.connect(host="localhost", user="cf-python", passwd="password")

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute(
    """CREATE TABLE IF NOT EXISTS Recipes(
    id             INT PRIMARY KEY AUTO_INCREMENT,
    name           VARCHAR(50),
    ingredients    VARCHAR(255),
    cooking_time   INT,
    difficulty     VARCHAR(20)
)"""
)


# Methods to do operations on the data of the task_database


# 1 - Code to create recipes


def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "easy"
        return difficulty
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "medium"
        return difficulty
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "intermediate"
        return difficulty
    elif cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "hard"
        return difficulty


def create_recipe(conn, cursor):
    try:
        name = str(input("Enter the name of the recipe: "))
        cooking_time = int(input("Enter the cooking time in minutes: "))
        ingredients_input = input(
            "Enter all the ingredients required for the recipe - each one being separated by a comma following by a space (bread, cheese, etc.)): "
        )
        ingredients = ingredients_input.split(", ")
        difficulty = calculate_difficulty(cooking_time, ingredients)
        recipe = {
            "name": name,
            "cooking_time": cooking_time,
            "ingredients": ingredients,
            "difficulty": difficulty,
        }

        sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
        # Since MySQL doesn’t fully support arrays, ingredients list needs to be converted into a \
        # comma-separated string, using .join
        val = (name, ", ".join(ingredients), cooking_time, difficulty)
        cursor.execute(sql, val)
        conn.commit()

        print("-----------------------")
        last_insert_id = cursor.lastrowid
        print("The ID of the newly inserted recipe is:", last_insert_id)
        print("Here is your newly created recipe: " + str(recipe))
        print("-----------------------")

    except:
        print("The input is incorrect or something went wrong.")


# 2 - Code to search recipes based on ingredients


def search_recipe(conn, cursor):
    all_ingredients = []

    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    # Convert the ingredients fetch from the database into strings
    for ingredients in results:
        ingredients_string = ingredients[0]
        ingredients = ingredients_string.split(", ")
        print(
            "These are the ingredients from the table as lists for each row"
            + str(ingredients)
        )

        for item in ingredients:
            print(
                "These are the ingredients from the table converted into string items:"
                + str(item)
            )
            if item not in all_ingredients:
                all_ingredients.append(item)

    print("-----------------------")

    # Display each ingredient to users, with a number on the side to make it easier for users to pick one
    for index, ingredient in enumerate(all_ingredients, start=1):
        print(str(index) + ". " + ingredient)

    search_ingredient = None

    # Ask users to pick a number related to an ingredients and launch a query to the database to \
    # display recipes containing this ingredient
    try:
        print("-----------------------")
        number_from_list = int(input("Pick a number from the list: ")) - 1
        search_ingredient = all_ingredients[number_from_list]
        print("-----------------------")
        print("Selected ingredient: " + search_ingredient)
        print("-----------------------")

        sql = "SELECT name, ingredients, cooking_time, difficulty FROM Recipes WHERE ingredients LIKE %s"
        val = ("%" + search_ingredient + "%",)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        print("Here are the recipes containing this ingredient:")
        for row in result:
            print(row)
    except:
        print("The input is incorrect or something went wrong.")


# 3 - Code to update recipes


def update_recipe(conn, cursor):
    cursor.execute(
        "SELECT id, name, ingredients, cooking_time, difficulty FROM Recipes"
    )
    result = cursor.fetchall()
    for row in result:
        print(
            "Recipe number: ", row[0])  # This is equal to recipe id, but renamed to by more user-friendly
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking time (min): ", row[3])
        print("Difficulty:", row[4])
        print()

    try:
        print("-----------------------")
        recipe_selected = int(
            input("Pick a recipe from the list based on its number: ")
        )
        print("-----------------------")
        print("Field possible to update for that recipe:")
        print("1. Name")
        print("2. Cooking time (min)")
        print("3. Ingredients")
        field_selected = int(
            input("Enter the number of the field you would like to update: ")
        )

        if field_selected == 1:
            updated_name = str(input("Enter the update name for this recipe: "))

            sql = "UPDATE Recipes SET name = %s WHERE id=%s"
            val = (updated_name, recipe_selected)
            cursor.execute(sql, val)
            conn.commit()

            print("Recipe name updated successfully!")

        if field_selected == 2:
            # First fetch the ingredients for the selected recipe from the database, to be able to pass \
            # them in the calculate_difficulty function call below, as this function require the cooking \
            # time and the ingredients of a recipe to work. This function is called in this block to ensure \
            # that the level of difficulty for a recipe is automatically update if necessary when cooking \
            # time is updated by users.
            cursor.execute(
                "SELECT ingredients FROM Recipes WHERE id = %s", (recipe_selected,)
            )
            results = cursor.fetchall()
            print(results)
            # When ingredients are fetched from database, they comes in following format: [('ing1, ing2',)] \
            # to ensure to pass the ingredients correctly in the calculate_difficulty function below \
            # the results[0][0] is used to access the string of ingredients and store it in ingredients_string \
            # variable.
            ingredients_string = results[0][0]
            # Line below is used to splits the string from ingredients_string into individual ingredients \
            # and stores them in a list, ensuring it can be passed correctly as an argument to calculate_difficulty
            ingredients = ingredients_string.split(", ")

            updated_cooking_time = int(
                input("Enter the updated cooking time (in min) for this recipe: ")
            )
            updated_difficulty = calculate_difficulty(updated_cooking_time, ingredients)

            sql_cooking_time = "UPDATE Recipes SET cooking_time = %s WHERE id=%s"
            val_cooking_time = (updated_cooking_time, recipe_selected)
            cursor.execute(sql_cooking_time, val_cooking_time)

            sql_difficulty = "UPDATE Recipes SET difficulty = %s WHERE id=%s"
            val_difficulty = (updated_difficulty, recipe_selected)
            cursor.execute(sql_difficulty, val_difficulty)

            conn.commit()

            print("Recipe cooking time updated successfully!")

        if field_selected == 3:
            # First fetch the cooking time for the selected recipe from the database, to be able to pass \
            # it in the calculate_difficulty function call below, as this function require the cooking \
            # time and the ingredients of a recipe to work. This function is called in this block to ensure \
            # that the level of difficulty for a recipe au automatically update if necessary when \
            # ingredients are updated by users.
            cursor.execute(
                "SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_selected,)
            )
            results = cursor.fetchall()
            # When cooking time is fetched from database, it comes in following format: [(-cooking time number,)] \
            # to ensure to pass the cooking time as in integer in the calculate_difficulty function below \
            # the results[0][0] is used to access the first element of the first tuple in the results \
            # variable, allowing to pass correctly the cooking time in the function, making everything work.
            cooking_time = results[0][0]

            ingredients_input = input(
                "Enter the updated ingredients for this recipe - each one being separated by a comma following by a space (bread, cheese, etc.)): "
            )
            updated_ingredients = ingredients_input.split(", ")
            updated_difficulty = calculate_difficulty(cooking_time, updated_ingredients)

            sql_ingredients = "UPDATE Recipes SET ingredients = %s WHERE id=%s"
            # Since MySQL doesn’t fully support arrays, your ingredients list needs to be converted into a \
            # comma-separated string, using .join
            val_ingredients = (", ".join(updated_ingredients), recipe_selected)
            cursor.execute(sql_ingredients, val_ingredients)

            sql_difficulty = "UPDATE Recipes SET difficulty = %s WHERE id=%s"
            val_difficulty = (updated_difficulty, recipe_selected)
            cursor.execute(sql_difficulty, val_difficulty)

            conn.commit()

            print("Recipe ingredients updated successfully!")

    except:
        print("The input is incorrect or something went wrong.")


# 4 - Code to delete recipes


def delete_recipe(conn, cursor):
    cursor.execute(
        "SELECT id, name, ingredients, cooking_time, difficulty FROM Recipes"
    )
    result = cursor.fetchall()
    for row in result:
        print(
            "Recipe number: ", row[0])  # This is equal to recipe id, but renamed to by more user-friendly
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking time (min): ", row[3])
        print("Difficulty:", row[4])
        print()

    try:
        print("-----------------------")
        recipe_selected = int(
            input("Pick a recipe to delete from the list based on its number: ")
        )

        sql = "DELETE FROM Recipes WHERE id=%s"
        val = (recipe_selected,)
        cursor.execute(sql, val)
        conn.commit()

        print("Recipe deleted successfully!")

    except:
        print("The input is incorrect or something went wrong.")


# Code to display the main menu to user


def main_menu():
    user_choice = None

    while user_choice != "quit":
        print("Main menu")
        print("-----------------------")
        print("Pick a choice")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredients")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print('Type "quit" to exit')
        user_choice = input('Your choice (pick a number or type "quit"): ')

        if user_choice == "1":
            create_recipe(conn, cursor)
            continue
        elif user_choice == "2":
            search_recipe(conn, cursor)
            continue
        elif user_choice == "3":
            update_recipe(conn, cursor)
            continue
        elif user_choice == "4":
            delete_recipe(conn, cursor)
            continue
        elif user_choice == "quit":
            conn.commit()
            conn.close()
            break

    print("The user chose: " + str(user_choice))


main_menu()
