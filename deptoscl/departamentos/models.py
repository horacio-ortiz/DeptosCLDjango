from django.db import models


# Create your models here.
class Depto(models.Model):
    '''Depto model, Proxy model extiende de base data '''

    Depto = models.TextField(blank=False)
    Direccion = models.TextField(blank=False)
    website = models.URLField(max_length=200, blank=True)
    Piso = models.CharField(max_length=20, blank=True)
    Ambientes = models.CharField(max_length=20, blank=True)
    Baños = models.CharField(max_length=20, blank=True)
    Metros_Tot = models.CharField(max_length=20, blank=True)
    Precio = models.CharField(max_length=20, blank=True)
    Fecha_visita = models.DateField(null=True)
    Observaciones_visita = models.TextField(blank=True)
    Numero_Contacto = models.CharField(max_length=20, blank=True)

    Foto = models.ImageField(upload_to='departamentos/pictures', blank=True, null=True)
    Pros = models.TextField(blank=True)
    Contras = models.TextField(blank=True)
    Creado = models.DateTimeField(auto_now_add=True)
    Modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return username'''
        return self.Depto
