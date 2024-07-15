from django.shortcuts import render, redirect
from django.http import Http404
from authors.forms import RegisterForm

# Create your views here.
def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    context = {
        'form':form
    }
    return render(request, 'authors/pages/register_view.html', context)

def register_create(request):
    if  not request.Post:
        raise Http404()
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)
    redirect('authors:register')
    