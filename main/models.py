from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from .manager import CustomerManager
from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Customer(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField('username', max_length=256)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomerManager()


    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def has_perm(self, perm, obj=None):
        if self.admin:
            return True

    def has_module_perms(self, app_label):
        if self.admin:
            return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.admin

    def __str__(self):
        return self.email
