from rest_framework import serializers

from authApp.models import User, New, Comment


class UserSerializer(serializers.ModelSerializer):
    '''serializador de usuarios'''
    class Meta:
        model = User
        fields = ['email', 'password', 'nombre',  'direccion', 'telefono', 'fecha_nacimiento']

    def create(self, validated_data):
        userInstace = User.objects.create(**validated_data)
        return userInstace
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'email': user.email,
            'nombre': user.nombre,
            'direccion': user.direccion,
            'telefono': user.telefono,
            'fecha_nacimiento': user.fecha_nacimiento
        }
    

class NewSerializer(serializers.ModelSerializer):
    '''Serializador de noticias'''
    class Meta:
        model = New
        fields = ['titulo', 'descripcion', 'owner']

    def to_representation(self, obj):   
        new = New.objects.get(id=obj.id)
        owner = User.objects.get(id=obj.owner_id)
        return {
            'id': new.id,
            'titulo': new.titulo,
            'descripcion': new.descripcion,
            'owner': {
                'id': owner.id,
                'email': owner.email,
                'nombre': owner.nombre
            },
            'fecha_publicacion': new.fecha_publicacion
        }


class CommentSerializer(serializers.ModelSerializer):
    '''Serializador de comentarios'''
    class Meta:
        model = Comment
        fields = ['comentario', 'owner', 'noticia'] # Corregir el modelo
 
    def to_representation(self, obj):
        comment = Comment.objects.get(id=obj.id)
        new = New.objects.get(id=obj.noticia_id)
        owner = User.objects.get(id=obj.owner_id)
        return {
            'id': comment.id,
            'comentario': comment.comentario,
            'owner': {
                'id': owner.id,
                'email': owner.email,
                'nombre': owner.nombre
            },
            'notica': {
                'id': new.id,
                'titulo': new.titulo
            },
            'fecha_publicacion': comment.fecha_publicacion
        }