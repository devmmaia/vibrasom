from django.db import models

# Create your models here.

class Song(models.Model):
    titulo = models.CharField(max_length=50)
    arquivo = models.FileField(upload_to='musicas/')

    def __str__(self):
        return self.titulo