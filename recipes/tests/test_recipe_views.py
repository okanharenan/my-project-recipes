from django.test import TestCase
from django.urls import resolve ,reverse
from recipes import views


class RecipeViewTest(TestCase):
    '''
    Teste das views de recipes

    '''
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_home_view_status_code_200_ok(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertEqual(response.status_code, 200)

    def test_home_view_loads_correct_template(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_home_view_shows_no_recipes_found_if_recipes(self):
         response = self.client.get(reverse("recipes:home"))
         self.assertIn('No recipes found here :/', response.content.decode('utf-8'))

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse("recipes:category", kwargs = {'id_category': 1}))
        self.assertIs(view.func, views.category)

    def test_category_view_status_code_200_ok(self):
        response = self.client.get(reverse("recipes:category", kwargs ={'id_category':1}))
        self.assertEqual(response.status_code, 404)


    def test_recipe_details_view_function_is_correct(self):
        view = resolve(reverse("recipes:recipes", kwargs = {'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_detail_view_status_code_404(self):
        response = self.client.get(reverse("recipes:recipes", kwargs = {'id': 1}))
        self.assertEqual(response.status_code, 404)