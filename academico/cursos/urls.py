# academico/cursos/urls.py
from django.urls import path
from . import views

app_name = 'cursos'
urlpatterns = [
    # /academico/cursos/  → lista de cursos
    path('', views.curso_list, name='list'),

    # /academico/cursos/<slug:slug>/  → detalle de curso y sub‑módulos
    path('<slug:slug>/', views.curso_detail, name='detail'),
]
