from django.db import models
#models == repository y model
class Usuario(models.Model):
    contraseña = models.CharField(max_length=128)
    fechaAlta = models.DateField(auto_now_add=True)
    nombreDeUsuario = models.CharField(max_length=50)
    correoElectronico = models.EmailField(max_length=50)

    class Meta:
        app_label = 'usuario'