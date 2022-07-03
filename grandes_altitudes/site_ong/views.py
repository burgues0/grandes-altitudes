from django.shortcuts import render
from .models import Feature

# Create your views here.
def index(request):
    featureX = Feature(18, "Victor", "Maluco brabo")
    featureY = Feature(100, "Carai", "Maluco doido")
    features = [featureX, featureY]
    return render(request, 'index.html', {'features': features})

def about(request):
    pass

def subjects(request):
    pass