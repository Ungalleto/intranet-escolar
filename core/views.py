from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.cache import never_cache
from django.urls import reverse_lazy

# ——— LOGIN personalizado ———
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return self.get_redirect_url() or reverse_lazy('dashboard')

# ——— DASHBOARD ———
@never_cache
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {
        'pendientes': get_pagos_pendientes(request.user),
        'aulas':      get_aulas(request.user),
        'cursos':     get_cursos(request.user),
        'ciclos':     get_ciclos(request.user),
    })

# ——— LOGOUT personalizado ———
@method_decorator(never_cache, name='dispatch')
class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'
