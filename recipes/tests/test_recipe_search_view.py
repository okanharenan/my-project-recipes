
from django.urls import resolve ,reverse
from recipes import views
from .test_recipe_base import RecipeTestBase

class RecipeSearchViewTest(RecipeTestBase):
    '''
    Teste das views de recipes
    '''

    def test_recipe_search_uses_correct_view_function(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse("recipes:search") + '?q=teste')
        self.assertTemplateUsed(response, "recipes/pages/search.html")

    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse('recipes:search') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404) 

    def test_recipes_search_term_is_on_page_and_escaped(self):
        url = reverse('recipes:search') + '?q=Teste'
        response = self.client.get(url)
        self.assertIn(
            'search for &quot;Teste&quot;',
            response.content.decode('utf-8')
        )
  
  
     
     
     
