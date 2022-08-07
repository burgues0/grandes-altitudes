from django.db import models

class UserLogin(models.Model):
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=500)
    # profile_pic = models.FileField()
    # possivel codigo pra guardar a imagem dos usuários no site
    occupation = models.CharField(max_length=30)

class Coordinator(models.Model):
    user_login = models.OneToOneField(UserLogin, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)

class Volunteer(models.Model):
    user_login = models.OneToOneField(UserLogin, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)

class Materials(models.Model):
    id_material = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    format = models.CharField(max_length=20)
    done_by = models.CharField(max_length=50)

class Reviews(models.Model):
    # nao tenho ctz dessa organização, mas imagino que um depoimento esteja atrelado a uma conta no site, correto?
    # caso a gente coloque tudo na mão, puxando imagem e perfil do insta ou algo do tipo, avisar por favor
    id_review = models.AutoField(auto_created=True, primary_key=True, default=1)
    user_login = models.ForeignKey(UserLogin, on_delete=models.CASCADE)
    reviewText = models.CharField(max_length=800)