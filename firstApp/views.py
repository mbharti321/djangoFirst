from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def myFunction(request):
    return HttpResponse("Hola World! How are you?")

def aboutUs(request):
    return HttpResponse("About Us... Hello! This is Manish Bharti.")

def functionAdd(request, a, b):
    return HttpResponse(a+b)

def functionIntro(request, name, age):
    return HttpResponse("Hello "+ name +"! Your age is " + str(age) + ".")

def functionIntro2(request, name, age):
    introDict = {
        "name": name,
        "age": age
    }
    return JsonResponse(introDict)