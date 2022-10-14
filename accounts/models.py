from email.policy import default
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
      
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            full_name=full_name,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    full_name = models.CharField(max_length=40)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # date_registerd = models.DateTimeField(auto_now_add = True)
    # date_joined = models.DateTimeField(auto_now = True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

 