from django.urls import path, include
from . import views

app_name = 'administrativo'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('aulas/', include('administrativo.aulas.urls', namespace='aulas')),
    path('biblioteca/', include('administrativo.biblioteca.urls', namespace='biblioteca')),
    path('ciclos/', include('administrativo.ciclos.urls', namespace='ciclos')),
    path('notas/', include('administrativo.notas.urls', namespace='notas')),
    path('pagos/', include('administrativo.pagos.urls', namespace='pagos')),
    path('usuarios/', include('administrativo.usuarios.urls', namespace='usuarios')),
]