from django.shortcuts import render
from django.http import HttpResponse

# Createyourviewshere.
def index(request):
    return HttpResponse("<h1> Bem-vindo(a) à aplicação IMC</h1>")

def calcular_imc(request,altura,peso):
    altura = altura/100.0
    response = f'Cálculo do IMC: {peso/(altura*altura)}'
    return HttpResponse(response)