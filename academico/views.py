# academico/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# sólo alumnos/profesores/pre-u
def es_academico(u):
    return u.is_authenticated and u.role in ['student','teacher','preu']

@login_required
@user_passes_test(es_academico, login_url='login')
def dashboard_academico(request):
    # puedes pasar listados generales si quieres
    return render(request, 'academico/dashboard.html')
