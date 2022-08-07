from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    last_three_reviews = Reviews.objects.all().order_by('id_review').reverse()[:3]
    return render(request, "index.html", {"reviews" : last_three_reviews})

def signup(request):
    return render(request, "signup.html")

def login(request):
    pass