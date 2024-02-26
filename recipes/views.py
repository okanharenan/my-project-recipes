from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipes

# Created view home 
def home(request):
    '''Criação da view home'''
    return render(request,'recipes/pages/home.html', context={
        'recipes': [make_recipes() for _ in range(10)]})

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipes(),
        'is_detail_page': True,
        
    })

def teste(request):
    return render(request, 'global/base.html')