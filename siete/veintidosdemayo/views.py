from django.shortcuts import render
from django.http import HttpResponse, JsonResponse




def index(request):
    
    return JsonResponse({'nombre': 'Leslie', 'novio': 'Arturo'})


# Create your views here.
