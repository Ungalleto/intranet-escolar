from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def foros_list(request):
    """Vista de listado para foros."""
    return render(request, 'academico/foros/list.html')