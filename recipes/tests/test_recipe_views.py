
from django.urls import resolve ,reverse
from recipes import views
from .test_recipe_base import RecipeTestBase
from recipes.models import RecipeModel
from unittest import skip
class RecipeViewTest(RecipeTestBase):

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

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse("recipes:category", kwargs = {'id_category': 1}))
        self.assertIs(view.func, views.category)

    def test_category_view_status_code_200_ok(self):
        self.make_recipe()
        response = self.client.get(reverse("recipes:category", kwargs ={'id_category':1}))
        self.assertEqual(response.status_code, 200)


    def test_recipe_details_view_function_is_correct(self):
        view = resolve(reverse("recipes:recipes", kwargs = {'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_detail_view_status_code_404(self):
        response = self.client.get(reverse("recipes:recipes", kwargs = {'id': 2}))
        self.assertEqual(response.status_code, 404)



    #test category views loads

    def test_recipe_category_template_loads_recipes(self):
         self.make_recipe()

         #need a recipe for this test
         response = self.client.get(reverse('recipes:category', args=(1,)))
         content = response.content.decode('utf-8')

         # check if one recipe exists
         self.assertIn("teste", content)
         

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        self.make_recipe()
        #need a recipe for this test
        response = self.client.get(reverse('recipes:recipes', kwargs={'id':1}))
        content = response.content.decode('utf-8')
        # check if one recipe exists
        self.assertIn("teste", content)
     

    
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
        
        
    def test_recipe_category_template_dont_load_not_published(self):
        self.make_recipe(is_published=False)
        '''
        testing recipes is published false dont show
        '''
        #need a recipe for this test
        response = self.client.get(reverse('recipes:recipes', kwargs={'id':1}))

        content = response.content.decode('utf-8')
        # check if one recipe exists
        self.assertEqual(response.status_code, 404)


    def test_recipe_detail_template_dont_load_not_published(self):

        recipes = self.make_recipe(is_published=False)
        '''
        testing recipes is published false dont show
        '''
        #need a recipe for this test
        response = self.client.get(reverse('recipes:recipes', kwargs={'id':recipes.id}))
        content = response.content.decode('utf-8')
        # check if one recipe exists
        self.assertEqual(response.status_code, 404)
  
  
  
     
     
     
