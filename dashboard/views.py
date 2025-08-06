from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests
from django.conf import settings

def index(request):

    response = requests.get(settings.API_URL)  # URL de la API // esta respuesta es sincrona.
    posts = response.json()  # Convertir la respuesta a JSON

    # Número total de respuestas
    total_responses = sum(value for key, value in posts.items() if key.isdigit())

    productoA = posts.get("1",0);
    productoB = posts.get("2",0);
    productoC = posts.get("3",0);
    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
        'productoA': productoA,
        'productoB': productoB, 
        'productoC': productoC,
    }
    return render(request, 'dashboard/index.html', data)