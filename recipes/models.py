from django.contrib.auth.models import User
from django.db import models

# Created model recipes

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name
class RecipeModel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None,)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=65)
    description = models.CharField(verbose_name="Descrição", max_length=165)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField(verbose_name="Tempo de prepro")
    preparation_time_unit =models.CharField(verbose_name="Preparação tempo de unidade", max_length=65)
    servings = models.CharField(verbose_name="Serve", max_length=3)
    servings_unit = models.CharField(verbose_name="serve Pessoas", max_length=65)
    preparation_step = models.CharField(verbose_name="Etapa de preparação", max_length=165)
    preparation_step_is_html = models.BooleanField(default="False")
    created_at = models.DateTimeField( auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField( default=False )
    cover = models.ImageField(upload_to="recipes/cover/%Y/%m/%d/", null=True, blank=True, default=False)

    def __str__(self):
        return self.title
        """
    Purpose: 
    """
    
  # end def