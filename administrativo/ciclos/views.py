from django.shortcuts import render

def ciclos_list(request):
    """Listado de ciclos."""
    return render(request, 'administrativo/ciclos/list.html')
