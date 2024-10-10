# By default, Django signals are executed synchronously. This means that when a signal is emitted, the receiver (the function connected to the signal) is executed immediately, in the same thread as the caller, before control returns to the caller.


import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.timezone import now

@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, **kwargs):
    print(f"Signal received at {now()}")
    time.sleep(5)  # Simulate a delay
    print(f"Signal finished at {now()}")

# Code to test it
def create_user_and_emit_signal():
    print(f"Caller starts at {now()}")
    user = User.objects.create(username="testuser")  # This will emit the post_save signal
    print(f"Caller finished at {now()}")

# Run this in a Django shell or view
create_user_and_emit_signal()