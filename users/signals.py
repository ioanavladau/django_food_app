from django.db.models.signals import post_save # get a signal when the user is registered
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User) # this fn will be called whenever it receives the post_save signal from the sender who is User 
def build_profile(sender, instance, created, **kwargs): #instance - the user to be saved, created-true/false, kwargs-additional arguments
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()




    



