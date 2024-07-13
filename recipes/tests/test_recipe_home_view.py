
from recipes import views
from django.urls import resolve ,reverse
from unittest.mock import patch
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
        response_recipe = response.context['recipe']

        # check if one recipe exists
        self.assertIn("teste", content)
        self.assertEqual(response_recipe.title, 'teste')
        

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

    
    def test_recipes_home_is_paginted(self):
        
        for i in range(3):
            kwargs = {'slug': f'u{i}', 'author_data': {'username': f'u{i}'} }
            self.make_recipe(**kwargs)
        
        with patch('recipes.views.PER_PAGE', new=1):
            response = self.client.get(reverse('recipes:home'))
            recipes = response.context['recipes']
            paginator = recipes.paginator
            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)),1)
            self.assertEqual(len(paginator.get_page(2)), 1)
            self.assertEqual(len(paginator.get_page(3)), 1)
            