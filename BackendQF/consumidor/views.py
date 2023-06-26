from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.shortcuts import render
from usuario.models import Usuario
from consumidor.models import Consumidor
class vistaConsumidor(View):
    def get(self, request, id=None):
        if id is None:
            consumidores = Consumidor.objects.all()
            response_data = {
                'message': 'Consumidores encontrados.',
                'consumidores': []
            }
            for consumidor in consumidores:
                consumidor_data = {
                    'nombre': consumidor.nombre,
                    'apellido': consumidor.apellido,
                    'fechaDeNacimiento':consumidor.fechaDeNacimiento,
                    'dni':consumidor.dni,
                    'localidad':consumidor.localidad,
                    'telefono':consumidor.telefono
                }
                response_data['consumidores'].append(consumidor_data)
        else:
            try:
                consumidor = Consumidor.objects.get(id=id)
                consumidor_data = model_to_dict(consumidor)
                response_data = {
                    'message': 'Consumidor encontrado',
                    'codigo':200,
                    'consumidor':consumidor_data
                }
            except Consumidor.DoesNotExist:
                consumidor_data = {
                    'message': 'Consumidor no encontrado.',
                    'codigo':400,
                    'consumidor': {},
                }
        return JsonResponse(response_data)