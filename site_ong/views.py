from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    subjects = ("Português","Matemática","História","Física","Quimica","Geografia","Filosofia","Sociologia",)
    return render(request, "index.html", {'subjects': subjects})

def about(request):
    pass

def subjects(request):
    pass