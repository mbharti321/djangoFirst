from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .forms import MyIntroForm


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


def functionIndex(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')

def temp(request):
    name = "Manish"
    languages = ['C', 'C++', 'Java', 'python']
    num1, num2 = 50, 10
    ans = num1 > num2
    tempDict = {
        "name" : name,
        "languages": languages,
        "num1" : num1,
        "num2" : num2,
        "ans" : ans,
    }
    return render(request, 'temp.html', context = tempDict)


def myImage(request):
    return render(request, 'myImage.html')

def myImage2(request):
    return render(request, 'myImage2.html')




def myForm(request):
    return render(request, 'myForm.html')

# For GET method
# def myFormResponse(request):
#     responseDict={
#         "FName": request.GET['text1'],
#         "LName": request.GET['text2'],
#         "method": request.method,
#     }
#     return JsonResponse(responseDict)


# For POST method
def myFormResponse(request):
    responseDict={
        "FName": request.POST['text1'],
        "LName": request.POST['text2'],
        "method": request.method,
    }
    return JsonResponse(responseDict)
    
    



# https://docs.djangoproject.com/en/3.1/topics/forms/ for reference
def myForm2(request):
    if request.method == 'POST':
        form = MyIntroForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/myFormResponse2/')
            # return HttpResponseRedirect( url 'myFormResponse2')
    else:
        form = MyIntroForm()

    return render(request, 'myForm2.html', {"form": form})


def myFormResponse2(request):
    responseDict={
        "FName": request.POST['firstName'],
        "LName": request.POST['lastName'],
        "method": request.method,
    }
    return JsonResponse(responseDict)