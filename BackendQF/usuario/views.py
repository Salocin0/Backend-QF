from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
from consumidor.models import Consumidor
import json
#views == logica de negocio
class vistaUsuario(View):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        consumidor_data = data.get('consumidor')
        usuario_data = consumidor_data.get('usuario') 

        usuario = Usuario.objects.create(
            contraseña=usuario_data['contraseña'],
            fechaAlta=usuario_data['fechaAlta'],
            nombreDeUsuario=usuario_data['nombreDeUsuario'],
            correoElectronico=usuario_data['correoElectronico']
        )

        consumidor = Consumidor.objects.create(
            nombre=consumidor_data['nombre'],
            apellido=consumidor_data['apellido'],
            fechaDeNacimiento=consumidor_data['fechaDeNacimiento'],
            dni=consumidor_data['dni'],
            localidad=consumidor_data['localidad'],
            telefono=consumidor_data['telefono'],
            usuario=usuario
        )

        response_data = {'message': 'Consumidor created successfully'}
        return JsonResponse(response_data)

    
    def get(self, request):
        data = json.loads(request.body.decode('utf-8'))
        nombre = data.get('nombre')
        response_data = {'message': 'get: Funciona'+nombre}
        return JsonResponse(response_data)

    

    
