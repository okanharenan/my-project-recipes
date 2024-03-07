from django.contrib import admin
from . models import RecipeModel, Category

def published(modeladmin, request, queryset ):
    queryset.update(is_published=True)
    
# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['category', 'is_published']
    actions=[published]


    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(RecipeModel, RecipeAdmin )
admin.site.register(Category, CategoryAdmin)