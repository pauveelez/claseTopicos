from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % (self.nombre)


class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length = 10, null= True)
    carrera = models.ForeignKey(Carrera, null=True)

    def __unicode__(self):
        return '%s: %s : %s' % (self.nombre, self.email, self.carrera)