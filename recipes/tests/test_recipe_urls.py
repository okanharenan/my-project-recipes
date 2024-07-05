from django.test import TestCase
from django.urls import reverse

class RecipeURlsTest(TestCase):
    def test_recipe_home_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipes_category_is_correct(self):
        category_url = reverse('recipes:category', kwargs={'id_category':1})
        self.assertEqual(category_url, '/recipes/category/1/')

    def test_recipes_detail_is_correct(self):
        url = reverse("recipes:recipes",  kwargs={'id':1})
        self.assertEqual(url, "/recipes/1/")

    def test_recipes_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')