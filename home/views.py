from django.shortcuts import render

# Create your views here.

def index(request):
    title = 'Home'
    return render(request, 'home/index.html', locals())

def adicionar(request):
    title = 'Adicionar'
    return render(request, 'home/adicionar.html', locals())
def concluido(request):
    title = 'concluido'
    return render(request, 'home/concluido.html', locals())




