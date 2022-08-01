from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    subjects = ("Português","Matemática","História","Física","Quimica","Geografia","Filosofia","Sociologia",)
    return render(request, "index.html", {'subjects': subjects})

def signup(request):
    return render(request, "signup.html")

def about(request):
    return render(request, "about.html")

def login(request):
    pass