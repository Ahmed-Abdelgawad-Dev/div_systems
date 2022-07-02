from email.policy import default
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import datetime
from .managers import AccountsManager
from django.core.exceptions import ValidationError
import os


def validate_avatar(value):
    ext              = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpeg''.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please upload images of type { jpg, jpeg, png } only.')

class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    DEFAULT_GENDER = 'male'
    GENDERS        = [('Male', 'male'), ('Female', 'female')]
    
    user_name    = models.CharField(max_length=255)
    
    first_name   = models.CharField(max_length=255,unique=True)
    last_name    = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    # Django-phonenumber-field => input string => E164 format in DB by default.
    phone_number = PhoneNumberField()
    gender       = models.CharField(choices = GENDERS,default = DEFAULT_GENDER, max_length = 50)
    birthdate    = models.DateField(_("Birthdate"), default = datetime.date(2010, 1, 1),auto_now_add = False,  auto_now= False)
    avatar       = models.FileField(upload_to='avatars/', default='default_image.png', validators=[validate_avatar])
    email        = models.EmailField(_('email address'), blank=True, null=True, help_text="Your Email...")
    
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    is_admin    = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = ['last_name', 'user_name']

    objects = AccountsManager()

    class Meta:
        verbose_name        = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return (self.first_name)

    def save(self, *args, **kwargs):
        if self.birthdate >= datetime.date.today():
            raise ValidationError(
                "Birthdate must be in the past.")
        super(CustomUser, self).save(*args, **kwargs)
    

