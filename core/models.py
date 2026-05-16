from django.db import models

class persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombres')
    apellido = models.CharField(max_length=100, verbose_name='Apellidos')
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    titulo_academico = models.CharField(max_length=100)
    biografia = models.TextField()
    correo_electronico = models.CharField(max_length=100)
    dedicacion = models.TextField()

    class Meta:
        db_table = 'persona'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre