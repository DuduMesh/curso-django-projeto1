from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Eduardo Prestes',
    })

def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return HttpResponse('Contato')
