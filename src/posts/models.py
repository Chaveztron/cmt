from django.db import models
from django.urls import reverse
from PIL import Image

class Tipo_Model(models.Model):
    tipo_model = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo_model

class tag(models.Model):
    tag = models.CharField(max_length=100)
    def __str__(self):
        return self.tag

# Create your models here.
class Post(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    edad = models.IntegerField()
    tag = models.ManyToManyField(tag)
    tipoModel = models.ForeignKey(Tipo_Model, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField()
    photoPortada = models.ImageField()
    photo1 = models.ImageField()
    photo2 = models.ImageField()
    photo3 = models.ImageField()
    photo4 = models.ImageField()
    photo5 = models.ImageField()
    photo6 = models.ImageField()
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('woman', kwargs={
            'id': self.id
        })

class Contacto(models.Model):
    telefono = models.IntegerField()
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.email

class Xl(models.Model):
    ip = models.TextField(null=True)
    contry = models.TextField(null=True)
    city = models.TextField(null=True)
    def __str__(self):
        return self.ip