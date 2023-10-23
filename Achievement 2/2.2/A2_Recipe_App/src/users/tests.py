from django.test import TestCase
from .models import User

# Create your tests here.

class UserModelTest(TestCase):
    def setUpTestData():
       # Set up non-modified objects used by some test methods
        User.objects.create(name='Testuser', email='testuser@gmail.com', notes='These are some notes')

    def test_user_name(self):
        # Get a recipe object to test
       user = User.objects.get(id=1)
       # Get the metadata for the 'name' field and use it to query its data
       field_label = user._meta.get_field('name').verbose_name
       # Compare the value to the expected result
       self.assertEqual(field_label, 'name')

    def test_user_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_user_email_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 75)
