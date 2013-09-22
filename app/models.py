from django.db import models

# Create your models here.
class estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()

    def __unicode__(self):
        return '%s: %s' % (self.nombre, self.email)