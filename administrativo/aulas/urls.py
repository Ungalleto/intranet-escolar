from django.urls import path
from . import views

app_name = 'aulas'  # debe coincidir con tu namespace

urlpatterns = [
    path('', views.aulas_list, name='list'),
]
