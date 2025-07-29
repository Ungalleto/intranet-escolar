from django.shortcuts import render

def biblioteca_list(request):
    """Listado de biblioteca."""
    return render(request, 'administrativo/biblioteca/list.html')
