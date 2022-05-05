from django.db import models

# Create your models here.
class Topnotch(models.Model):
    word = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    personA = models.TextField()
    personB = models.TextField()
    sentences =models.TextField()
    grammar = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Course(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='course/img/%y/%m/%d')
    vids = models.FileField(upload_to='course/vids/%y/%m/%d')
    audio = models.FileField(upload_to='course/audio/%y/%m/%d')




