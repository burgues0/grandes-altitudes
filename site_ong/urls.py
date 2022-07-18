from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    # path("materias", views.materias, name="materias"),
    # path("signup", views.signup, name="signup"),
    # path("signup", views.signup, name="signup"),
    # path("signup", views.signup, name="signup"),
    # path("signup", views.signup, name="signup"),
]