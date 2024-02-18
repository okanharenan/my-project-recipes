from django.shortcuts import render
from django.http import HttpResponse

# Created view home 
def home(request):
    '''Criação da view home'''
    return render(request,'recipes/pages/home.html')