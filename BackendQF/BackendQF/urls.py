from django.contrib import admin
from django.urls import path
from django.views.decorators.http import require_http_methods
from usuario.views import vistaUsuario
from django.views.decorators.http import require_POST, require_GET
#url == router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', vistaUsuario.as_view(), name='ABMC_usuario'),
]
