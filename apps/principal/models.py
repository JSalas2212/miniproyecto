from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre