from django.contrib import admin
from django.urls import path
from .Views.views import FuncionaView
from django.views.decorators.http import require_http_methods
from .Views.usuario_view import vistaUsuario
from django.views.decorators.http import require_POST, require_GET
#url == router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('funciona/', require_http_methods(["GET"])(FuncionaView.as_view()), name='get_funciona'),
    path('user/', vistaUsuario.as_view(), name='crear_usuario'),
]
