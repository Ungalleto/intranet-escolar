from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def evaluaciones_list(request):
    """Listado general de evaluaciones."""
    return render(request, 'academico/evaluaciones/list.html')