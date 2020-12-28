from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def myFunction(request):
    return HttpResponse("Hola World! How are you?")
