from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ..Models.consumidor_model import Consumidor
import json
#views == logica de negocio
class vistaUsuario(View):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        nombre,apellido, = data.get('nombre','apellido')
        consumidor= Consumidor()
        
        consumidor.save
        response_data = {'message': 'POST: Funciona'+nombre}
        return JsonResponse(response_data)
    
    def get(self, request):
        data = json.loads(request.body.decode('utf-8'))
        nombre = data.get('nombre')
        response_data = {'message': 'get: Funciona'+nombre}
        return JsonResponse(response_data)

    

    
