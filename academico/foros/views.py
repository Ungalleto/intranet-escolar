from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def app_list(request):
    return render(request, 'academico/foros/list.html')  # ajusta el path
