from django.contrib import admin
from django.urls import path
from .Views.views import FuncionaView
from django.views.decorators.http import require_http_methods

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funciona/', require_http_methods(["GET"])(FuncionaView.as_view()), name='get_funciona'),
    path('funciona/', require_http_methods(["POST"])(FuncionaView.as_view()), name='post_funciona'),
    path('funciona/', require_http_methods(["PUT"])(FuncionaView.as_view()), name='put_funciona'),
    path('funciona/', require_http_methods(["DELETE"])(FuncionaView.as_view()), name='delete_funciona'),
]
