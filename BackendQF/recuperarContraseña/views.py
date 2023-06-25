from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.shortcuts import render
from usuario.models import Usuario
from recuperarContraseña.models import RecuperarContraseña
import hashlib
from django.core.mail import send_mail
# Create your views here.
class VistaRecuperarContraseña(View):
    def put(self, request,codigo=None):
        if codigo is None:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('correoElectronico')
            try:
                user = Usuario.objects.get(correoElectronico=email)
                codigo = hashlib.sha256(email.encode('utf-8')).hexdigest()[:50]
                try:
                    recuperarContraseña = RecuperarContraseña.objects.get(codigo=codigo)
                except RecuperarContraseña.DoesNotExist:
                    RecuperarContraseña.objects.create(usuario=user, codigo=codigo)
                send_mail(
                    'Recuperar contraseña',  # Asunto del correo
                    'Se solicitó un cambio de contraseña. Para cambiar tu contraseña, haz clic en el siguiente enlace: http://127.0.0.1:8000/user/recuperarContraseña/' + str(codigo),  # Cuerpo del correo
                    'quickfoodrecuperacion@gmail.com',  # Dirección de correo electrónico del remitente
                    [user.correoElectronico],  # Lista de direcciones de correo electrónico de los destinatarios
                    fail_silently=False,  # Indica si mostrar o no excepciones en caso de error
                )

                response_data = {
                    'message': 'email enviado',
                    'user': {},
                }
            except Usuario.DoesNotExist:
                response_data = {
                    'error':'usuario no existe',
                    'codigo':1010
                }
        else:
            data = json.loads(request.body.decode('utf-8'))
            contraseña = data.get('contraseña')
            try:
                recuperarContraseña= RecuperarContraseña.objects.get(codigo=codigo)
                user = Usuario.objects.get(correoElectronico=recuperarContraseña.usuario.correoElectronico)
                user.contraseña = contraseña
                user.save()
                recuperarContraseña.delete()
                response_data = {
                    'message': 'contraseña actualizada.',
                }
            except RecuperarContraseña.DoesNotExist:
                response_data = {
                    'error':'no existe peticion para recuperar contraseña',
                    'codigo':1010
                } 
        return JsonResponse(response_data)