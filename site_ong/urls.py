from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("donate", views.donate, name="donate"),
    path("subjects", views.subjects, name="subjects"),
    # path("signup", views.signup, name="signup"),
    # path("signup", views.signup, name="signup"),
    # path("signup", views.signup, name="signup"),
    # path("signup", views.signup, name="signup"),
]