from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404, HttpResponse
from utils.recipes.factory import make_recipes
from .models import RecipeModel

# Created view home 
def home(request,):
    '''Criação da view home'''

    recipe = RecipeModel.objects.filter(is_published=True).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipe
    })

def category(request, id_category):
    recipe = get_list_or_404(RecipeModel.objects.filter(
        category__id=id_category,
        is_published=True,
    ).order_by('-id') )
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipe,
        'title': f'{recipe[0].category.name} - category |',
    })

def recipe(request, id):
   
    recipe = get_object_or_404(RecipeModel,pk = id, is_published = True )
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
        
    })

def teste(request):
    return render(request, 'global/base.html')

def search(request):
    search_term = request.GET.get("q")
    if not search_term:
        raise Http404()
    return render(request, 'recipes/pages/search.html')