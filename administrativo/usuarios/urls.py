from django.urls import path
from . import views


app_name = 'usuarios'

urlpatterns = [
    path('', views.usuarios_list, name='list'),
]