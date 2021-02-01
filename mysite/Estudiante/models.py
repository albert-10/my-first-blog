from django.db import models

# Create your models here.

NOTAS = (
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

class Estudiante(models.Model):
    nombre = models.CharField(max_length = 30)
    apellidos = models.CharField(max_length = 30)
    numeroIdentidad = models.CharField(max_length = 11, unique = True)
    nota = models.IntegerField(choices = NOTAS)
    numeroTelefono = models.IntegerField()

    def __str__(self):
        return self.nombre