from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AccountsManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        # if not email:
        #     raise ValueError(_('Email must be set'))
        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)

    # def create_user(self, email, date_of_birth, password=None):
    #     if not email:
    #         raise ValueError('Please Enter an Email address to continue')

    #     user = self.model(
    #         email=self.normalize_email(email),
    #         date_of_birth=date_of_birth,
    #     )

    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    # def create_superuser(self, email, date_of_birth, password=None):
    #     user = self.create_user(
    #         email,
    #         password=password,
    #         date_of_birth=date_of_birth,
    #     )
    #     user.is_admin = True
    #     user.save(using=self._db)
    #     return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    DEFAULT_GENDER = 'Male'
    GENDERS = [('Male', 'male'), ('Female', 'female')]
    username = models.CharField(
        max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(
        max_length=255)
    country_code = models.CharField(max_length=255)
    # phone_number =
    gender = models.CharField(
        choices=GENDERS,
        default=DEFAULT_GENDER, max_length=50
    )
    birthdate = models.DateField(null=True, blank=True)
    # avatar = models.ImageField(upload_to='avatars/', required=True)
    email = models.EmailField(
        _('email address'), unique=True, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    objects = AccountsManager()

    def __str__(self):
        return ("{} {}".format(self.first_name, self.last_name))

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
