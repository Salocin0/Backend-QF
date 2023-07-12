from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
from consumidor.models import Consumidor
from django.forms.models import model_to_dict
import json
#views == logica de negocio
class vistaUsuario(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            consumidor_data = data.get('consumidor')
            usuario_data = consumidor_data.get('usuario') 

            usuario = Usuario.objects.create(
                contraseña=usuario_data['contraseña'],
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

            response_data = {
                'message': 'Consumidor created successfully',
                'code':200
            }
        except Exception as e:
            print(str(e))
            response_data = {
                'message': 'Error al guardar',
                'code': 400
            }
        return JsonResponse(response_data)

    def get(self, request, id=None):
        if id is None:
            usuarios = Usuario.objects.all()
            response_data = {
                'message': 'Usuarios encontrados.',
                'usuarios': []
            }
            for usuario in usuarios:
                usuario_data = {
                    'id': usuario.id,
                    'nombreDeUsuario': usuario.nombreDeUsuario,
                    'fechaAlta':usuario.fechaAlta,
                    'correoElectronico':usuario.correoElectronico
                }
                response_data['usuarios'].append(usuario_data)
        else:
            try:
                user = Usuario.objects.get(id=id)
                user_data = model_to_dict(user)
                response_data = {
                    'message': 'Usuario encontrado',
                    'user':user_data
                }
            except Usuario.DoesNotExist:
                response_data = {
                    'message': 'Usuario no encontrado.',
                    'user': {},
                }
        return JsonResponse(response_data)