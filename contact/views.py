from django.shortcuts import render
from contact.models import Contact
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def index(request):
    title = 'Home'
    contacts = Contact.objects.all()
    return render(request, 'contact/index.html', locals())


@login_required(login_url='/login/')
def adicionar(request):
    title = 'Adicionar'
    return render(request, 'contact/adicionar.html', locals())


@login_required(login_url='/login/')
def concluido(request):
    title = 'concluido'
    return render(request, 'contact/concluido.html', locals())




