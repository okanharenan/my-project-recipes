from django.contrib import admin
from . models import RecipeModel, Category

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['category']
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(RecipeModel, RecipeAdmin )
admin.site.register(Category, CategoryAdmin)