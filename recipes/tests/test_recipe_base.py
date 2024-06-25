from django.test import TestCase
from recipes.models import Category, RecipeModel , User


class RecipeTestBase(TestCase):
    def setUp(self):
        self.make_recipe()
        return super().setUp()
    

    def makeCategory(self, name = "category"):
        return Category.objects.create(name = name)

    def makeAuthor(self,
        first_name = "user",
        last_name = "name",
        username = "Renan",
        password = "123456",
        email = "user@email.com",
    ):
        return User.objects.create_user(
        first_name = first_name,
        last_name = last_name,
        username = username,
        password = password,
        email = email,
        )
    

    def make_recipe(self,
                      title = "teste",
                      description = "Somente um teste",
                      slug = "teste",
                      preparation_time = 1,
                      preparation_time_unit = "2",     
                      servings = "2",
                      servings_unit = "4",
                      preparation_step = "teste das recipes",
                      preparation_step_is_html = False,
                      is_published = True,
                      category_data = None,
                      author_data = None,
                      ):
        
        if category_data is None:
            category_data = {}
        if author_data is None:
            author_data = {}

        return RecipeModel.objects.create(
             title = title,
             description = description,
             slug = slug,
             preparation_time = preparation_time,
             preparation_time_unit = preparation_time_unit,
                     
             servings = servings,
             servings_unit = servings_unit,
             preparation_step = preparation_step,
             preparation_step_is_html = preparation_step_is_html,
             is_published = is_published,
             category = self.makeCategory(**category_data),
             author = self.makeAuthor(**author_data),

        ) 
    