from django.db import models
#models == repository y model
class Usuario(models.Model):
    contraseña = models.PasswordField()
    fechaAlta = models.DateField(auto_now_add=True)
    nombreDeUsuario = models.CharField(max_length=50)
    correoElectronico = models.EmailField(max_length=50)