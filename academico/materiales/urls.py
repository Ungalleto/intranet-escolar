# academico/materiales/urls.py
from django.urls import path
from . import views

app_name = 'materiales'   # ← así coincide con namespace='materiales'

urlpatterns = [
    path('', views.materiales_list, name='list'),
    # …
]
