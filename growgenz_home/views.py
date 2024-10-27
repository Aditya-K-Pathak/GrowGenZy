from django.shortcuts import render, HttpResponse
import json
from .sender import TEMPLATE, Mail

# Create your views here.

def index(request):
    if request.method == 'POST':
        # print(request.POST)
        mail = TEMPLATE.replace('username', request.POST.get('fname'))
        Mail().sendMail(request.POST.get('email'), mail)
        return HttpResponse(f'Dear {request.POST.get('fname')}, We have received your response.')
    with open('secrets.json', 'r') as file:
        data = json.load(file)
    return render(request, 'index.html', context = data)