# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .models import CustomUser


# @receiver(pre_save, sender=CustomUser)
# def auto_rename_user(sender, instance, **kwargs):
#     user = instance
#     if user.first_name == '' and user.phone_number is not None:
#         user.first_name = 'Anonymous'
