from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.shortcuts import render
from usuario.models import Usuario
from consumidor.models import Consumidor
from funcionesNavbar.models import FuncionesNavbar


class vistaFuncionesNavbar(View):
    def get(self, request, id):
        try:
            usuario = Usuario.objects.get(id=id)
            acciones = FuncionesNavbar.objects.get(usuario=usuario)
            response_data = {
                'message': 'acciones encontradas',
                'codigo': 200,
                'acciones':acciones.acciones
            }
        except Usuario.DoesNotExist or FuncionesNavbar.DoesNotExist:
            consumidor_data = {
                'message': 'acciones no encontradas.',
                'codigo': 400,
                'acciones': {},
            }
        return JsonResponse(response_data)
