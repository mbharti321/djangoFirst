from django.urls import path
from . import views

urlpatterns=[
    path('',views.myFunction, name = "home"),
    
    path('aboutUs', views.aboutUs, name = "aboutUs"),
    path('add/<int:a>/<int:b>', views.functionAdd, name = "addMe"),
    path('intro/<str:name>/<int:age>', views.functionIntro, name = "intro"),
    path('intro2/<str:name>/<int:age>', views.functionIntro2, name = "intro2"),

    path('index', views.functionIndex, name = "index"),
    path('about', views.about, name = "about"),
    path('temp', views.temp, name = 'temp'),
    path('myImage', views.myImage, name = 'myImage'),
    path('myImage2', views.myImage2, name = 'myImage2'),
    path('myForm', views.myForm, name = 'myForm'),


    path('myFormResponse', views.myFormResponse, name = 'myFormResponse'),
]