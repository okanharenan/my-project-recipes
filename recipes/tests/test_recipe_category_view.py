
from django.urls import resolve ,reverse
from recipes import views
from .test_recipe_base import RecipeTestBase

class RecipeCategoryViewTest(RecipeTestBase):
    '''
    Teste das views de recipes
    '''
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse("recipes:category", kwargs = {'id_category': 1}))
        self.assertIs(view.func, views.category)

    def test_category_view_status_code_200_ok(self):
        self.make_recipe()
        response = self.client.get(reverse("recipes:category", kwargs ={'id_category':1}))
        self.assertEqual(response.status_code, 200)

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

    def test_recipe_category_template_loads_recipes(self):
         self.make_recipe()

         #need a recipe for this test
         response = self.client.get(reverse('recipes:category', args=(1,)))
         content = response.content.decode('utf-8')

         # check if one recipe exists
         self.assertIn("teste", content)
         


