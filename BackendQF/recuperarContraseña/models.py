from django.db import models
from usuario.models import Usuario
#models == repository y model
class RecuperarContraseña(models.Model):
    codigo = models.CharField(max_length=100)
    usuario = models.OneToOneField(Usuario,on_delete=models.CASCADE)

    class Meta:
        app_label = 'recuperarContraseña'