from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    '''Manejador de usuarios'''

    def create_user(self, email, password=None):
        '''Para la creacion de usuarios'''
        
        if not email:
            raise ValueError('Agregue su email')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user
    

    def create_superuser(self, email, password):
        '''Creacion de super usuarios'''

        user = self.create_user(
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)

        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    '''Modelo de usuarios'''
    id = models.AutoField(primary_key=True)
    email = models.EmailField('Email', max_length=60, unique=True)
    password = models.CharField('Password', max_length=100)
    nombre = models.CharField('Nombre', max_length=50)
    direccion = models.CharField('Dirección', max_length=40)
    telefono = models.IntegerField('Télefono')
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    is_active = models.BooleanField(default=True)

    def save(self, **kwargs):
        '''Hasheando o ponerle más seguridad a la contraseña a la hora de guardarse en la DB'''
        some_salt = 'L4sa6Na'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'email'