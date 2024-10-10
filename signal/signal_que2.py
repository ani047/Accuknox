# Question 2: Do Django signals run in the same thread as the caller?
# Answer: Yes, Django signals run in the same thread as the caller by default.

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, **kwargs):
    print(f"Signal thread ID: {threading.get_ident()}")

# Code to test it
def create_user_and_emit_signal():
    print(f"Caller thread ID: {threading.get_ident()}")
    user = User.objects.create(username="testuser")

# Run this in a Django shell or view
create_user_and_emit_signal()