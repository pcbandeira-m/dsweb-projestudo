from django.shortcuts import render
from django.http import HttpResponse

# Variáveis globais da enquete
PERGUNTA = "Qual o seu gênero musical preferido?"
ALTERNATIVAS = ["rock", "indie", "pop", "folk"]

def index(request):
    context = {
        'pergunta': PERGUNTA,
        'alternativas': ALTERNATIVAS,
    }
    return render(request, 'index.html', context)

def votar(request):
    return HttpResponse("OI, VOTO REGISTRADO!")