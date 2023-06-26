from django.db import models
#models == repository y model
class Usuario(models.Model):
    contraseña = models.CharField(max_length=128)#minimo 6 caracteres
    fechaAlta = models.DateField(auto_now_add=True)
    nombreDeUsuario = models.CharField(max_length=50)
    correoElectronico = models.EmailField(max_length=50)
    
    #se requiere que el e-mail no se repita, es decir, que no exista otro usuario con el mismo e-mail.
    class Meta:
        app_label = 'usuario'