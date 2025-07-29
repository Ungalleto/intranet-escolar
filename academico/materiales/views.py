from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def materiales_list(request):
    """Listado de materiales."""
    return render(request, 'academico/materiales/list.html')