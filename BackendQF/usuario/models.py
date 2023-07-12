from django.db import models
from django.core.validators import MinLengthValidator

class Usuario(models.Model):
    contraseña = models.CharField(max_length=128, validators=[MinLengthValidator(6)])  # Mínimo 6 caracteres
    fechaAlta = models.DateField(auto_now_add=True)
    nombreDeUsuario = models.CharField(max_length=50)
    correoElectronico = models.EmailField(max_length=50, unique=True)  # Se requiere que el e-mail no se repita

    class Meta:
        app_label = 'usuario'
