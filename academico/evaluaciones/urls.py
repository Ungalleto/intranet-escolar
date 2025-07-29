from django.urls import path
from . import views

app_name = 'evaluaciones'

urlpatterns = [
    path('', views.evaluaciones_list, name='list'),
    # path('<int:pk>/', views.evaluacion_detail, name='detail'),
]
