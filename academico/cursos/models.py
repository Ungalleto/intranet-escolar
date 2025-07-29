from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre


class SubModulo(models.Model):
    curso = models.ForeignKey(Curso, related_name="submodulos", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo