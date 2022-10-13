from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("signup", views.signup, name="signup"),
    #path("signin", views.signin, name="signin"),
    path("about", views.about, name="about"),
    path("subjects", views.subjects, name="subjects"),
    path("donate", views.donate, name="donate"),
    path("reviews", views.reviews, name="reviews"),
]