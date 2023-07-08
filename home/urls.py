from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('concluido/', views.concluido, name='concluido'),
]
