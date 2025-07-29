from django.shortcuts import render

def pagos_list(request):
    """Listado de pagos."""
    return render(request, 'administrativo/pagos/list.html')