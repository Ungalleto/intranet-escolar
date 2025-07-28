# academico/urls.py
from django.urls import path, include
from . import views

app_name = 'academico'

urlpatterns = [
    # Dashboard del módulo académico
    path('', views.dashboard_academico, name='dashboard'),

    # Submódulos
    path('materiales/', include('academico.materiales.urls',
                                namespace='materiales')),
    path('foros/',       include('academico.foros.urls',
                                namespace='foros')),
    path('evaluaciones/',include('academico.evaluaciones.urls',
                                namespace='evaluaciones')),
    path('comunicaciones/', include('academico.comunicaciones.urls',
                                   namespace='comunicaciones')),

    # Cursos y sus sub‑unidades
    path('cursos/', include('academico.cursos.urls',
                            namespace='cursos')),
]
