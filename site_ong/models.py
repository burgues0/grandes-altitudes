from datetime import date
from django.db import models

class UserCredentials(models.Model):
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=500)
    # profile_pic = models.FileField()
    # possivel codigo pra guardar a imagem dos usuários no site
    occupation = models.CharField(max_length=30)

class Coordinator(models.Model):
    user_login = models.OneToOneField(UserCredentials, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)

class Volunteer(models.Model):
    user_login = models.OneToOneField(UserCredentials, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)

class Materials(models.Model):
    id_material = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    format = models.CharField(max_length=20)
    author = models.CharField(max_length=50)

class Reviews(models.Model):
    # nao tenho ctz dessa organização, mas imagino que um depoimento esteja atrelado a uma conta no site, correto?
    # caso a gente coloque tudo na mão, puxando imagem e perfil do insta ou algo do tipo, avisar por favor
    id_review = models.AutoField(primary_key=True)
    user_login = models.ForeignKey(UserCredentials, on_delete=models.CASCADE)
    reviewText = models.CharField(max_length=800)
    date_add = models.DateField(default=date.today)

    """ # Uma ideia pra tentar automatizar a questão dos depoimentos.
class Depoimento: #isso deve haver em models.py
        name: str
        formation: str
        details: str
        is_true: bool


    depoimento1 = depoiment()
    depoimento1.name = 'Julio Vasconcelos'
    depoimento1.formação = 'UFRJ'
    depoimento1.details = 'GRATA A ONG....'
    ...
    depoimento2 = depoiment()
    depoimento3 = depoiment()
    

    depoiments = [depoimento1, depoimento2, depoimento3]

    #in page of depoiments
    {% for depoiment in depoiments %} 
        {{depoimento.name}}
        {{depoimento1.formação = 'UFRJ'}}
        {{depoimento.details}}
    {% end for %} """