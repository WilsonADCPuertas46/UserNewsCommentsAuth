from django.db import models

from .user import User


class New(models.Model):
    '''Modelo de noticias'''
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=100)
    descripcion = models.TextField('Descripción')
    owner = models.ForeignKey(User, related_name='news', on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField('Fecha de publicacion', auto_now_add=True)

    class Meta:
        ordering = ['fecha_publicacion']