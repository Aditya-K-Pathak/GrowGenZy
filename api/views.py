import json
from . import gen_ai
from rest_framework import response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['post'])
def getResponse(request):
    data = list(request.data['chat'])
    return response.Response(gen_ai.model_response(data=data))