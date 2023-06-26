from django.contrib import admin
from django.urls import path
from django.views.decorators.http import require_http_methods
from usuario.views import vistaUsuario
from login.views import vistaLogin
from django.views.decorators.http import require_POST, require_GET
from recuperarContraseña.views import VistaRecuperarContraseña
from consumidor.views import vistaConsumidor
#url == router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', vistaUsuario.as_view(), name='ABMC_usuario'),
    path('user/<int:id>/', vistaUsuario.as_view(), name='get_usuario_by_id'),
    path('consumidor/', vistaConsumidor.as_view(), name='ABMC_usuario'),
    path('consumidor/<int:id>/', vistaConsumidor.as_view(), name='get_usuario_by_id'),
    path('user/login/', vistaLogin.as_view(), name='user-login'),
    path('user/recuperarcontrasenia/', VistaRecuperarContraseña.as_view(), name='user-recuperar-contrasenia'),
    path('user/recuperarcontrasenia/<str:codigo>/', VistaRecuperarContraseña.as_view(), name='user-recuperar-contrasenia'),
]
