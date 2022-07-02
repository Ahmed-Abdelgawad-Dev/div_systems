from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import CustomUser


@receiver(pre_save, sender=CustomUser)
def auto_rename_user(sender, instance, **kwargs):
    user = instance
    if user.user_name == '':
        #Generate a username from first&last_name
        user.user_name = str(user.first_name).capitalize() + \
            " " + str(user.last_name).capitalize()
