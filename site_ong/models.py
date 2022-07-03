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