from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import datetime
from .managers import AccountsManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    DEFAULT_GENDER = 'Male'
    GENDERS = [('Male', 'male'), ('Female', 'female')]
    first_name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(
        max_length=255,  unique=True)
    country_code = models.CharField(max_length=255)
    # input string => E164 format in DB by default
    # https://pypi.org/project/django-phonenumber-field/
    phone_number = PhoneNumberField()
    gender = models.CharField(
        choices=GENDERS,
        default=DEFAULT_GENDER, max_length=50
    )
    birthdate = models.DateField(
        _("Birthdate"), default=datetime.date(2010, 1, 1),
        auto_now_add=False, auto_now=False)
    avatar = models.ImageField(
        upload_to='avatars/', default='images/default_image.png')
    email = models.EmailField(
        _('email address'), unique=True, blank=True, null=True, help_text="Please enter your Email...")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = ['last_name']

    objects = AccountsManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return ("{} {}".format(self.first_name, self.last_name))

    def save(self, *args, **kwargs):
        if self.birthdate >= datetime.date.today():
            raise ValidationError(
                "The date must be in the past at least by one day")
        super(CustomUser, self).save(*args, **kwargs)
