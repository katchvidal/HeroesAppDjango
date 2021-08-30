from django.db import models
from django.utils import timezone

# Create your models here.

class Heroe(models.Model):

    Character = models.CharField( max_length=255 )
    Publisher = models.CharField( max_length=255 )
    Alter_ego = models.CharField( max_length=255 )
    First_appearence = models.CharField( max_length=255 )
    imagen = models.FileField(upload_to='heroes', default='settings.MEDIA_ROOT/media/logo192.png')

    def __str__(self):
        return self.Publisher
    