from django.shortcuts import render

def aulas_list(request):
    """Vista simple de Aulas."""
    return render(request, 'administrativo/aulas/list.html')