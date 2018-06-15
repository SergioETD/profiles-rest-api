from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.UserProfile) #Poner el modelo que creamos
admin.site.register(models.ProfileFeedItem)
