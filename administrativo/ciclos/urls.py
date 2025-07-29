from django.urls import path
from . import views


app_name = 'ciclos'

urlpatterns = [
    path('', views.ciclos_list, name='list'),
]