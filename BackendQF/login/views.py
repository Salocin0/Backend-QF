from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.shortcuts import render
from usuario.models import Usuario
class vistaLogin(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('correoElectronico')
        contraseña = data.get('contraseña')
        try:
            user = Usuario.objects.get(correoElectronico=email)
            if(user.contraseña==contraseña):
                response_data = {
                    'authenticated': True,
                    'error':'',
                    'codigo':200
                    }
            else:
                response_data = {
                    'authenticated': False,
                    'error':'Contraseña incorrecta',
                    'codigo':1000
                }
        except Usuario.DoesNotExist:
            response_data = {
                    'authenticated': False,
                    'error':'Email incorrecto',
                    'codigo':1010
                }
        return JsonResponse(response_data)