from django.shortcuts import render

def usuarios_list(request):
    """Listado de usuarios."""
    return render(request, 'administrativo/usuarios/list.html')