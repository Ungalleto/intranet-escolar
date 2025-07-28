# academico/cursos/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from academico.cursos.models import Curso, SubModulo

def es_academico(u):
    return u.is_authenticated and u.role in ['student','teacher','preu']

@login_required
@user_passes_test(es_academico, login_url='login')
def curso_list(request):
    cursos = Curso.objects.all()  # o filtrar por usuario
    return render(request, 'academico/cursos/list.html', {'cursos': cursos})

@login_required
@user_passes_test(es_academico, login_url='login')
def curso_detail(request, slug):
    curso = get_object_or_404(Curso, slug=slug)
    # asumimos que tienes un modelo SubModulo con FK a Curso
    submodulos = SubModulo.objects.filter(curso=curso)
    return render(request,
                  'academico/cursos/detail.html',
                  {'curso': curso, 'submodulos': submodulos})
