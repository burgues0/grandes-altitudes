from django.db import models

class user_login(models.Model):
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=500)
    occupation = models.CharField(max_length=20)

class coordinator(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    email = models.OneToOneField(user_login, on_delete=models.CASCADE, primary_key=True)

class volunteer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    email = models.OneToOneField(user_login, on_delete=models.CASCADE, primary_key=True)

class materials(models.Model):
    id_material = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    format = models.CharField(max_length=20)
    done_by = models.CharField(max_length=50)


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