# Question 3: By default, do Django signals run in the same database transaction as the caller?
# Answer: Yes, Django signals are part of the same database transaction by default. If the transaction is rolled back, any changes made by the signal receiver will also be rolled back.

from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Assuming we have a Profile model linked to User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

# Signal to create a Profile when a User is saved
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print("Signal receiver is creating a profile")
        Profile.objects.create(user=instance)

# Code to test the behavior inside a transaction
def create_user_and_rollback():
    try:
        with transaction.atomic():  # Start a transaction
            user = User.objects.create(username="testuser")
            print("User created, signal triggered to create profile")
            raise Exception("Rolling back transaction")  
    except Exception as e:
        print(f"Exception occurred: {e}")


create_user_and_rollback()