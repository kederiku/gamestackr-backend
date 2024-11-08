from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from gamestackr.accounts.manager import AccountManager


class Account(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    image = models.ImageField(upload_to='account', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    object = AccountManager()  # noqa A003

    class Meta:
        verbose_name = 'Account'
