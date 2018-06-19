from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with our new custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object"""

        if not email:
            raise ValueError('Users must have an email')

        email = self.normalize_email(email) #Normaliza la cadena de email, es decir, pone todo en minusculas
        user = self.model(email = email, name = name)

        user.set_password(password)
        user.save(using=self._db) #Significa que se va a usar la misma BD que se creó para guardar al objeto user

        return user #Retorna el objeto


    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details"""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Respents a user profile inside our system"""

    email = models.EmailField(max_length=255, unique=True) #Captura el correo
    name = models.CharField(max_length=255) #Captura el nombre
    is_activate = models.BooleanField(default=True) #Determina si el usuario está actualmente activo
    is_staff = models.BooleanField(default=False) #Para impedir que lleguen nuevos usuarios como autorizados

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' #El valor que se va a ocupar como usrname, con el cual se hara el log in

    """Required fields"""

    REQUIRED_FIELDS = ['name'] #Email ya es requerido en el field, por eso no se coloca aquí

    def get_full_name(self):  # "def" define una función
        """Used to get a users full name"""
        return self.name

    def get_short_name(self):
        """Used to get a users short name"""
        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""
        return self.email

class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey('UserProfile', on_delete = models.CASCADE)
    status_text  = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        """Return the model as a string"""

        return self.status.text
