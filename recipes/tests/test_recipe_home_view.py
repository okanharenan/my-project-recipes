
from django.urls import resolve ,reverse
from recipes import views
from .test_recipe_base import RecipeTestBase

class RecipeHomeViewTest(RecipeTestBase):
    '''
    Teste das views de recipes
    '''
    def test_recipe_home_view_function_is_correct(self):
        self.make_recipe()
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        #need a recipe for this test
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_recipe = response.context['recipes']

        # check if one recipe exists
        self.assertIn("teste", content)
        self.assertEqual(response_recipe.first().title, 'teste')
        

    def test_home_view_status_code_200_ok(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertEqual(response.status_code, 200)

    def test_home_view_loads_correct_template(self):
        self.make_recipe()
        response = self.client.get(reverse("recipes:home"))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    #@skip("teste se a recipes pulado")
    def test_home_view_shows_no_recipes_found_if_recipes(self):
         self.make_recipe(is_published=False)
         response = self.client.get(reverse("recipes:home"))
         self.assertIn('No recipes found here :/', response.content.decode('utf-8'))
    
    
    def test_recipe_home_template_dont_load_not_published(self):
        self.make_recipe(is_published=False)
        '''
        testing recipes is published false dont show
        '''
        #need a recipe for this test
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        # check if one recipe exists
        self.assertIn('No recipes found here :/', response.content.decode('utf-8'))