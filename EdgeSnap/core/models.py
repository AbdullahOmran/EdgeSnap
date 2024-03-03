from django.db import models
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_delete
import os 

# Create your models here.

class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    out_image = models.ImageField(upload_to='images/', null=True, blank=True)

@receiver(pre_delete, sender=UserImage)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
    if instance.out_image:
        if os.path.isfile(instance.out_image.path):
            os.remove(instance.out_image.path)