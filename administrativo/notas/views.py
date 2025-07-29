from django.shortcuts import render

def notas_list(request):
    """Listado de notas."""
    return render(request, 'administrativo/notas/list.html')