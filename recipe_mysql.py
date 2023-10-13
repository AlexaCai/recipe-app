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


# Methods to do operations on the data of this database

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
    name = str(input("Enter the name of the recipe: "))
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients_input = input(
        "Enter all the ingredients required for the recipe - each one being separated by a comma following by a space (bread, cheese, etc.)): "
    )
    ingredients_split = ingredients_input.split(", ")
    ingredients = ", ".join(ingredients_split)
    difficulty = calculate_difficulty(cooking_time, ingredients)
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty,
    }

    sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (name, ingredients, cooking_time, difficulty)
    cursor.execute(sql, val)
    conn.commit()

    print("-----------------------")
    last_insert_id = cursor.lastrowid
    print("The ID of the newly inserted recipe is:", last_insert_id)
    print("Here is your newly created recipe: " + str(recipe))
    print("-----------------------")


# 2 - Code to search recipes based on ingredients

def search_recipe(conn, cursor):
    all_ingredients = []

    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()  

    for ingredients in results:
        ingredients_string = ingredients[0]  
        ingredients = ingredients_string.split(', ')  
        print('These are the ingredients from the table as lists for each row' + str(ingredients))

        for item in ingredients:
                print('These are the ingredients from the table converted into string items:' + str(item))
                if item not in all_ingredients:
                    all_ingredients.append(item)
    print('This is the list of all ingredient in ingredient_list: ' + str(all_ingredients))
    print("-----------------------")




#     def update_recipe(conn, cursor):


#     def delete_recipe(conn, cursor):


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
