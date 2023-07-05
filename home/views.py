from django.shortcuts import render

# Create your views here.

def index(request):
    title = 'Home'
    return render(request, 'home/index.html', locals())
