
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class FuncionaView(View):
    def get(self, request):
        response_data = {'message': 'GET: Funciona'}
        return JsonResponse(response_data)

    def post(self, request):
        response_data = {'message': 'POST: Funciona'}
        return JsonResponse(response_data)

    def put(self, request):
        response_data = {'message': 'PUT: Funciona'}
        return JsonResponse(response_data)

    def delete(self, request):
        response_data = {'message': 'DELETE: Funciona'}
        return JsonResponse(response_data)