
from django.urls import resolve ,reverse
from recipes import views
from .test_recipe_base import RecipeTestBase

class RecipeDetailViewTest(RecipeTestBase):
    '''
    Teste das views de recipes
    '''
    def test_recipe_details_view_function_is_correct(self):
        view = resolve(reverse("recipes:recipes", kwargs = {'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_detail_view_status_code_404(self):
        response = self.client.get(reverse("recipes:recipes", kwargs = {'id': 2}))
        self.assertEqual(response.status_code, 404)

         

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        self.make_recipe()
        #need a recipe for this test
        response = self.client.get(reverse('recipes:recipes', kwargs={'id':1}))
        content = response.content.decode('utf-8')
        # check if one recipe exists
        self.assertIn("teste", content)
     

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


   
  
  
     
     
     
