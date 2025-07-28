# intranet/urls.py
from django.contrib import admin
from django.urls import path, include
from core.views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth personalizado (login POST / logout POST)
    path('accounts/login/',
         CustomLoginView.as_view(), name='login'),
    path('accounts/logout/',
         CustomLogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    # Módulos grandes
    path('academico/', include('academico.urls',
                               namespace='academico')),
    #path('administrativo/', include('administrativo.urls',
    #                                namespace='administrativo')),

    # Dashboard genérico u otras rutas
    path('', include('core.urls')),
]
