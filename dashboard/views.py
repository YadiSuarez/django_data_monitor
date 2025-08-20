from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required('dashboard.index_viewer', raise_exception=True)
def index(request):

    response = requests.get(settings.API_URL)
    posts = response.json()

    # Total de votos
    total_responses = sum(value for key, value in posts.items() if key.isdigit())

    # Datos de productos
    productos = [
        {"nombre": "Diseño de Samurai", "votos": posts.get("1", 0)},
        {"nombre": "Diseño de Joker",   "votos": posts.get("2", 0)},
        {"nombre": "Diseño de Medusa",  "votos": posts.get("3", 0)},
    ]

    # Calcular porcentajes y añadirlos al diccionario
    for producto in productos:
        if total_responses > 0:
            producto["porcentaje"] = str(round(producto["votos"] / total_responses * 100, 2))+ "%"
        else:
            producto["porcentaje"] = 0.0

    data = {
        "title": "Landing Page' Dashboard",
        "total_responses": total_responses,
        "productos": productos,
    }
    return render(request, 'dashboard/index.html', data)