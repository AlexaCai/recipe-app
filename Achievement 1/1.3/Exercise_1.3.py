recipes_list = []
ingredients_list = []

def take_recipe ():
    name = str(input("Enter the name of the recipe: "))
    cooking_time = int(input("Enter the cooking time in minutes: "))
    # Each ingredient are added following a comma, and this comma is then used to split each ingredient into an item in the list.
    ingredients_input = str(input("Enter all the ingredients required for the recipe - each one being separated by a comma): "))
    ingredients = ingredients_input.split(', ')
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    return recipe

number_of_recipes = int(input("Enter how many recipes you would like to create: "))
n = number_of_recipes

for number_recipe_specified in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)
    for ingredient in recipe['ingredients']:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)

for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        difficulty = 'easy'
        recipe['difficulty'] = 'easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'medium'
        recipe['difficulty'] = 'medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        difficulty = 'intermediate'
        recipe['difficulty'] = 'intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'hard'
        recipe['difficulty'] = 'hard'

for recipe in recipes_list:
    print("Recipe: " + recipe['name'])
    print("Cooking time (min): " + str(recipe['cooking_time']))
    print('Ingredients:')
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print("Difficulty level: " + recipe['difficulty'])

ingredients_list.sort()
print('Ingredients available across all recipes:')
for ingredients in ingredients_list:
    print(ingredients)