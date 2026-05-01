from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def calcular(request):
    if request.method == 'GET':
        return render(request,'erro.html')
    altura = float(request.POST.get('altura'))
    peso = float(request.POST.get('peso'))

    # altura = altura/100

    imc = peso/(altura*altura)

    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif imc < 24.9:
        classificacao = 'Peso normal'
    elif imc < 29.9:
        classificacao = 'Sobrepeso'
    else:
        classificacao = 'Obesidade'
    contexto = {
        'imc': imc,
        'classificacao': classificacao,
        'altura': altura,
        'peso': peso,
    }
    return render(request, 'resultado_imc.html', contexto)