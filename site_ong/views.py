from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    subjects = ("Português","Matemática","História","Física","Quimica","Geografia","Filosofia","Sociologia",)
    return render(request, "index.html", {'subjects': subjects})

def register(request):
    return render(request, "register.html")

def subjects(request):
    pass