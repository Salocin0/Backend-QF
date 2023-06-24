from django.db import models
from usuario.models import Usuario
from django.core.exceptions import ValidationError
#models == repository y model
class Consumidor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaDeNacimiento = models.DateField()#validators=[validarFechaNacimiento]
    dni = models.IntegerField()
    localidad = models.CharField(max_length=50)
    telefono = models.IntegerField()
    usuario = models.OneToOneField(Usuario,on_delete=models.CASCADE)

    def validarFechaNacimiento(fechaDeNacimiento):
        fecha_actual = datetime.now().date()
        if fechaDeNacimiento >= fecha_actual:
            raise ValidationError("Error con la fecha de nacimiento mayor a la actual")
        else:
            return True

    class Meta:
        app_label = 'consumidor'

    
        