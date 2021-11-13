from django.db import models

# Create your models here.

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80,null=False)
    contenido = models.CharField(max_length=80,null=False)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo