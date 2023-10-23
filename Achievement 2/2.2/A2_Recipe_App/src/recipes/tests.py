from django.test import TestCase
from .models import Recipe

# Create your tests here.

class RecipeModelTest(TestCase):
    def setUpTestData():
       # Set up non-modified objects used by some test methods
        Recipe.objects.create(name='Tacos al pastor', description='Tacos al pastor are mexican tacos that can be found around all Mexico and many other countries', cooking_time='45', ingredients='tortillas, meat, salsa, coriander', cooking_instructions='Here are the cooking instructions', category='mexican', creation_date='2020-10-10')

    def test_recipe_name(self):
       # Get a recipe object to test
       recipe = Recipe.objects.get(id=1)
       # Get the metadata for the 'name' field and use it to query its data
       field_label = recipe._meta.get_field('name').verbose_name
       # Compare the value to the expected result
       self.assertEqual(field_label, 'name')

    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_recipe_time_data_type(self):
        recipe = Recipe.objects.get(id=1)
        data_type = isinstance(recipe.cooking_time, int)
        self.assertTrue(data_type)

    def test_recipe_ingredients_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('ingredients').max_length
        self.assertEqual(max_length, 255)

    def test_calculate_difficulty_easy(self):
        # Create a recipe with cooking time and ingredients for an easy difficulty
        recipe = Recipe(cooking_time=5, ingredients="ingredient1, ingredient2, ingredient3")
        # Calculate the difficulty
        difficulty = recipe.calculate_difficulty(recipe.cooking_time, recipe.ingredients)
        # Check if the calculated difficulty is "easy"
        self.assertEqual(difficulty, "easy")

    def test_calculate_difficulty_medium(self):
        recipe = Recipe(cooking_time=5, ingredients="ingredient1, ingredient2, ingredient3, ingredient4")
        difficulty = recipe.calculate_difficulty(recipe.cooking_time, recipe.ingredients)
        self.assertEqual(difficulty, "medium")

    def test_calculate_difficulty_intermediate(self):
        recipe = Recipe(cooking_time=45, ingredients="ingredient1, ingredient2, ingredient3")
        difficulty = recipe.calculate_difficulty(recipe.cooking_time, recipe.ingredients)
        self.assertEqual(difficulty, "intermediate")

    def test_calculate_difficulty_hard(self):
        recipe = Recipe(cooking_time=45, ingredients="ingredient1, ingredient2, ingredient3, ingredient4")
        difficulty = recipe.calculate_difficulty(recipe.cooking_time, recipe.ingredients)
        self.assertEqual(difficulty, "hard")