from django.shortcuts import render
from django.http import HttpResponse

# Createyourviewshere.
def index(request):
    return HttpResponse("<h1> Bem-vindo(a) à aplicação IMC</h1>")