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
    path("subjects/matematica", views.subj_mat, name="matematica"),
    path("subjects/portugues", views.subj_port, name="portugues"),
    path("subjects/redacao", views.subj_red, name="redacao"),
    path("subjects/quimica", views.subj_qui, name="quimica"),
    path("subjects/fisica", views.subj_fis, name="fisica"),
    path("subjects/biologia", views.subj_bio, name="biologia"),
]