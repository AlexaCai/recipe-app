class Recipe(object):
    ingredients_list = []

    def __init__(self, name):
        self.name = name
        self.cooking_time = 0
        self.ingredients = []
        self.difficulty = ""

    def calculate_difficulty(self, cooking_time, ingredients):
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

    def get_name(self):
        output = "Recipe: " + str(self.name)
        return output

    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        output = "Cooking time (min): " + str(self.cooking_time)
        return output

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        # Line below ensure that if the cooking time is updated / changed, the function calculating \
        # difficulty will get triggered again to display any change in the difficulty if necessary
        self.difficulty = self.calculate_difficulty(self.cooking_time, self.ingredients)

    # Using an asterisk * before the argument ingredients to make it a variable-length arguments and allow to enter multiple ingredients at the same time
    # *ingredients create a tuple out of the user input, wheter there's only one ingredient added or more
    def add_ingredients(self, *ingredients):
        # This line iterates through each element in the tuple, treating them as individual strings
        # This allow to work with ingredients added by users as strings up to this point, not tuple anymore
        for ingredient in ingredients:
            if ingredient not in self.ingredients:
                self.ingredients.append(ingredient)
                self.update_all_ingredients()
                # Ensure that if the ingredients are updated / changed, the function calculating difficulty \
                # will get triggered again to display any change in the difficulty if necessary
                self.difficulty = self.calculate_difficulty(
                    self.cooking_time, self.ingredients
                )
            else:
                print(
                    "You tried to add "
                    + str(ingredient)
                    + " in the recipe' list of ingredients, but this ingrdient is already in it, so has not been added again"
                )

    def get_ingredients(self):
        output = self.ingredients
        return output

    def get_difficulty(self):
        if self.difficulty == "":
            self.difficulty = self.calculate_difficulty(
                self.cooking_time, self.ingredients
            )
            output = "Recipe difficulty: " + self.difficulty
            return output
        else:
            output = "Recipe difficulty: " + self.difficulty
            return output

    def search_ingredient(self, ingredients_searched):
        for ingredients in self.ingredients:
            if ingredients == ingredients_searched:
                return True
        else:
            return False

    def update_all_ingredients(self):
        for ingredients in self.ingredients:
            if not ingredients in Recipe.ingredients_list:
                Recipe.ingredients_list.append(ingredients)

    def __str__(self):
        output = (
            "Name of the recipe: "
            + str(self.name)
            + "\nCooking time (min): "
            + str(self.cooking_time)
            + "\nIngredients: "
            + str(self.ingredients)
            + "\nDifficulty: "
            + str(self.difficulty)
        )
        return output

    def recipe_search(data, search_term):
        # If data is not a list (so if the search is made trough only one recipe - not a list) \
        # convert it to a list so the following operations can be carried on
        if not isinstance(data, list):
            data = [data]

        for recipe in data:
            if recipe.search_ingredient(search_term) is True:
                print(recipe)


# ADDING OBJECTS TO THE LIST

tea = Recipe("Tea")
tea.add_ingredients("Tea leaves", "Sugar", "Water", "Salt")
tea.set_cooking_time(35)
tea.get_difficulty()

print(tea)