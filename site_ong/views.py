from ast import Sub
import os
from tokenize import String
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from decouple import config
import pyrebase

fbConfig = {
    "apiKey": config("API_KEY"),
    "authDomain": config("AUTH_DOMAIN"),
    "projectId": config("PROJECT_ID"),
    "storageBucket": config("STORAGE_BUCKET"),
    "messagingSenderId": config("MESSAGING_SENDER_ID"),
    "appId": config("APP_ID"),
    "serviceAccount": {config("FIREBASE_JSON")},
    "databaseURL": os.path.abspath(os.path.dirname(__file__)) + config("FIREBASE_DATABASE_URL")
}

firebase = pyrebase.initialize_app(fbConfig)
auth = firebase.auth()


# Create your views here.
def index(request):
    last_three_reviews = Reviews.objects.all().order_by('id_review').reverse()[:3]
    return render(request, "index.html", {"reviews" : last_three_reviews})

#cadastro de usuarios
def signup(request):
    #caso o metodo seja post, o formulario foi enviado
    if(request.method == "POST"):
        #salva os valores do form em variaveis
        userEmail = request.POST["email"]
        userPassword = request.POST["password"]
        passwordConf = request.POST["password-confirm"]
        #checa pra ver se a senha e a mesma da confirmação
        if(userPassword == passwordConf):
            #!!!
            #!!!
            #OBS.: implementar dps uma funcao pra checagem de senha forte, e a comparacao da senha com a confirmacao de senha (pra substituir essa comparacao dentro desse if)
            #!!!
            #!!!
            #checa na base de dados caso o email recebido no form já existe, se sim redireciona de volta para a pagina
            if(UserCredentials.objects.filter(email=userEmail).exists()):
                messages.info(request, "Email já foi utilizado.")
                return redirect("signup")
            #caso o username e o email sejam novos, ele cria o usuario, salva no BD e redireciona pra pagina de login
            else:
                firebaseUser = auth.create_user_with_email_and_password(userEmail, userPassword)
                uid = firebaseUser['localId']
                idtoken = request.session['uid']
                mainDatabaseUser = UserCredentials.objects.create(email=userEmail, password=userPassword)
                mainDatabaseUser.save()
                return render(request, "signin.html")
        else:
            messages.info(request, "As senhas não batem.")
            return redirect("signup")
    else:
        return render(request, "signup.html")

#login dos usuarios
def signin(request):
    if(request.method == "POST"):
        userEmail = request.POST["email"]
        userPassword = request.POST["password"]
        try:
            firebaseUser = auth.sign_in_with_email_and_password(userEmail, userPassword)
        except:
            messages.info(request, "Credenciais inválidas.")
            return redirect("signin")
        firebaseUser = auth.refresh(firebaseUser['refreshToken'])
        sessionID = firebaseUser['idToken']
        request.session['uid'] = str(sessionID)
        print(firebaseUser)
        return redirect("index")
    return render(request, "signin.html")

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "signin.html")

def about(request):
    return render(request, "about.html")

def subjects(request):

    class Subject:
        def __init__(self, title, icon, url, desc, color):
            self.title = title
            self.desc = desc
            self.icon = icon
            self.url = url
            self.color = color

    dados_materias = {
        "Matemática" : {
            'desc': 'tamo junto wellington!',
            'icon': 'fa-solid fa-square-root-variable fa-5x center_icon_card',
            'url': '/subjects/matematica',
            'color': '#73CEE3'
        },
        "Português" : {
            'desc': 'aline sz gustavo!',
            'icon': 'fa-solid fa-pen-to-square fa-5x center_icon_card',
            'url': '/subjects/portugues',
            'color': '#73CEE3'
        },
        "Redação" : {
            'desc': 'aytel for president!',
            'icon': 'fa-solid fa-book-open fa-5x center_icon_card',
            'url': '/subjects/redacao',
            'color': '#73CEE3'
        },
        "Química" : {
            'desc': 'odemar king!',
            'icon': 'fa-solid fa-atom fa-5x center_icon_card',
            'url': '/subjects/quimica',
            'color': '#73CEE3'
        },
        "Física" : {
            'desc': 'juliana e mini juliana!',
            'icon': 'fa-solid fa-brain fa-5x center_icon_card',
            'url': '/subjects/fisica',
            'color': '#73CEE3#73CEE3'
        },
        "Biologia" : {
            'desc': 'wilber: o que é a vida!',
            'icon': 'fa-solid fa-dna fa-5x center_icon_card',
            'url': '/subjects/biologia',
            'color': '#73CEE3'
        },
    }

    materias = []

    for key in dados_materias.keys():
        materias.append(Subject(key, dados_materias[key]['icon'], dados_materias[key]['url'], dados_materias[key]['desc'], dados_materias[key]['color']))

    return render(request, "subjects.html", {"materias" : materias})

def donate(request):
    num_agencia = 420420
    num_conta = 696969
    return render(request, "donate.html")

def reviews(request):
    return render(request, "reviews.html")
