from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class AccountsManager(BaseUserManager):
    def create_user(self, first_name, password, **extra_fields):
        user = self.model(first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(first_name, password, **extra_fields)
