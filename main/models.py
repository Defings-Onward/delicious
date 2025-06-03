from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(unique=True, max_length=100)
    image = models.ImageField(upload_to='images')
    note = models.TextField()

class Chef(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    quote = models.CharField( max_length=100)
    facebook_name = models.CharField(null=True, max_length=100)
    instagram_name = models.CharField(null=True, max_length=100)
    in_name = models.CharField(null=True, max_length=100)
    x_name = models.CharField(null=True, max_length=100)

class Occasion(models.Model):
    picture = models.ImageField(upload_to='images')
    head = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    para1 = models.TextField()
    dot1 = models.TextField()
    dot2 = models.TextField()
    dot3 = models.TextField()
    para2 = models.TextField()


class Testimonies(models.Model):
    picture= models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    rate = models.FloatField()
    comment = models.TextField()

class MenuType(models.Model):
    name = models.CharField(max_length=100)


class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    type = models.ForeignKey(MenuType, on_delete=models.CASCADE)



class Table(models.Model):
    name = models.CharField(default="User", max_length=200)
    email = models.EmailField(default="example@gmail.com")
    phone = models.CharField(null=True, max_length=200)
    date = models.DateTimeField()
    message = models.TextField()
    read = models.BooleanField(default=True)


class Contact(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
# Create your models here.
