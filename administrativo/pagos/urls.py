from django.urls import path
from . import views


app_name = 'pagos'

urlpatterns = [
    path('', views.pagos_list, name='list'),
]