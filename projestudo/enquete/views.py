from django.shortcuts import render

total1=0
total2=0
total3=0
total4=0

def index(request):
    contexto = {
        'pergunta': 'Qual é o seu gênero musical favorito?',
        'alternativa1': 'Rock',
        'alternativa2': 'Indie',
        'alternativa3': 'Pop',
        'alternativa4': 'Folk',
    }
    return render(request, 'index2.html', contexto)

def votar(request):
    global total1, total2, total3, total4
    resposta = request.GET.get('alternativa')
    if resposta == '1':
        total1 += 1
    elif resposta == '2':
        total2 += 1
    elif resposta == '3':
        total3 += 1
    elif resposta == '4':
        total4 += 1

    total_votos= total1 + total2 + total3 + total4

    contexto = {
        'alternativa1': 'Rock',
        'alternativa2': 'Indie',
        'alternativa3': 'Pop',
        'alternativa4': 'Folk',
        'total1': total1,
        'total2': total2,
        'total3': total3,
        'total4': total4,
        'total_votos': total_votos,
    }
    return render(request, 'resultado2.html', contexto)