from django.db.models.signals import post_save # The signal
from django.contrib.auth.models import User # The sender
from django.dispatch import receiver # The receiver
from .models import Profile
# User here in this case will be what we call "THE SENDER" that is sending the signal
# We also have to create a receiver who is a function that get the signal and then performs some path

# Receiver is the decorater that it can add our function
# This reciver decorator takes the signal we want and the sender
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Now we create the save prifile function
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# Last step is to import those functions in function ready in the user apps.py file