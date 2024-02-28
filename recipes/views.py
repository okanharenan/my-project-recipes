from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipes
from .models import RecipeModel

# Created view home 
def home(request,):
    '''Criação da view home'''
    recipe = RecipeModel.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipe
    })

def category(request, id_category):
    '''Criação da view home'''
    recipe = RecipeModel.objects.filter(category__id=id_category).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipe
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipes(),
        'is_detail_page': True,
        
    })

def teste(request):
    return render(request, 'global/base.html')