from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def comunicaciones_list(request):
    """Listado básico de comunicaciones."""
    return render(request, 'academico/comunicaciones/list.html')
