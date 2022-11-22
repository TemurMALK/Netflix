from django.contrib.auth.models import User
from django.db import models


class Aktyor(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=30)
    tugilgan_yil = models.DateField()
    davlat = models.CharField(max_length=30)
    def __str__(self):return self.ism

class Kino(models.Model):
    nom = models.CharField(max_length=30)
    yil = models.DateField()
    reyting = models.FloatField()
    janr = models.CharField(max_length=30)
    aktyorlar = models.ManyToManyField(Aktyor)
    def __str__(self):return self.nom

class Comment(models.Model):
    izoh = models.CharField(max_length=30)
    sana = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    def __str__(self):return self.izoh
