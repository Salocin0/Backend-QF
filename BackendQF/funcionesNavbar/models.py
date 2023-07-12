from django.db import models
from usuario.models import Usuario

class FuncionesNavbar(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    acciones = models.TextField(blank=True, null=True)

    def clean(self):
        if self.acciones:
            acciones_list = self.acciones.split(',')
            if len(acciones_list) > 10:
                raise ValidationError('El número máximo de acciones permitidas es 10.')

    class Meta:
        app_label = 'funcionesNavbar'

