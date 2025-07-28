from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ESTUDIANTE = 'student'
    MAESTRO   = 'teacher'
    ADMIN     = 'admin'
    PREU       = 'preu'
    ROLE_CHOICES = [
        (ESTUDIANTE, 'Estudiante'),
        (MAESTRO,   'Maestro'),
        (ADMIN,     'Administrador'),
        (PREU,       'Preuniversitario'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ESTUDIANTE)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
