
from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import RecipeTestBase , RecipeModel, Category

class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def make_recipe_no_default(self):
        recipe = RecipeModel(
            category=self.make_category(name = "Test is Default is False"),
            author=self.make_author(username="username is Renan"),
            title='teste',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_step='Recipe Preparation Steps',
            preparation_step_is_html=False,
            is_published=False,
    )
        recipe.full_clean()
        recipe.save()
        return recipe
    
    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_default()
        self.assertFalse(recipe.is_published,
                         msg="recipe is_published is not false")
        
    def test_recipe_string_representation(self):
        needed = 'Testing Representation'
        self.recipe.title = needed
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe), needed,
            msg=f'Recipe string representation must be '
                f'"{needed}" but "{str(self.recipe)}" was received.'
        )

       