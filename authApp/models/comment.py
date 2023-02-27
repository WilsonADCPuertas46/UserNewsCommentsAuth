from django.db import models

from . import User, New


class Comment(models.Model):
    '''Modelo de usuarios'''
    id = models.AutoField(primary_key=True)
    comentario = models.CharField('Comentario', max_length=250)
    owner = models.ForeignKey(User, related_name='comentario_owner', on_delete=models.CASCADE)
    noticia = models.ForeignKey(New, related_name='comentario_new', on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField('Fecha de publicacion', auto_now_add=True)

    class Meta:
        ordering = ['fecha_publicacion']