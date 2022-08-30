from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import pyrebase
from decouple import config

fbConfig = {
    "apiKey": config("API_KEY"),
    "authDomain": config("AUTH_DOMAIN"),
    "projectId": config("PROJECT_ID"),
    "storageBucket": config("STORAGE_BUCKET"),
    "messagingSenderId": config("MESSAGING_SENDER_ID"),
    "appId": config("APP_ID"),
    "serviceAccount": config("FIREBASE_CREDENTIALS")
}

firebase = pyrebase.initialize_app(fbConfig)
auth = firebase.auth()
fbDatabase = firebase.database()

# Create your views here.
def index(request):
    last_three_reviews = Reviews.objects.all().order_by('id_review').reverse()[:3]
    return render(request, "index.html", {"reviews" : last_three_reviews})

def signup(request):
    return render(request, "signup.html")

def login(request):
    pass

def about(request):
    return render(request, "about.html")

def subjects(request):
    return render(request, "subjects.html")

def donate(request):
    return render(request, "donate.html")

def reviews(request):
    return render(request, "reviews.html")