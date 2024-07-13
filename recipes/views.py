import os
from django.db.models import Q
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404, HttpResponse
from utils.recipes.factory import make_recipes
from utils.recipes.pagination import make_pagination
from .models import RecipeModel
from django.core.paginator import Paginator

PER_PAGE = os.environ.get('PER_PAGE', 6)

# Created view home 
def home(request,):

    recipe = RecipeModel.objects.filter(is_published=True).order_by('-id')
  
    page_obj, pagination_range = make_pagination(request, recipe, PER_PAGE)
    return render(request, 'recipes/pages/home.html', context={
        'recipes':page_obj,
        'pagination_range':pagination_range,
})

def category(request, id_category):
    recipe = get_list_or_404(RecipeModel.objects.filter(
        category__id=id_category,
        is_published=True,
    ).order_by('-id') )

    page_obj, pagination_range = make_pagination(request, recipe, PER_PAGE)
    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_obj,
        'pagination_range':pagination_range,
        'title': f'{recipe[0].category.name} - category |',
    })

def recipe(request, id):
   
    recipe = get_object_or_404(RecipeModel, pk = id, is_published = True )

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
        
    })

def teste(request):
    return render(request, 'global/base.html')

def search(request):
    search_term = request.GET.get("q", '').strip()
    if not search_term:
        raise Http404()
    
    recipes = RecipeModel.objects.filter(
        Q(
            Q(title__icontains = search_term) |
            Q(description__icontains = search_term),
        ), 
        is_published = True    
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'search for "{search_term}" |',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })