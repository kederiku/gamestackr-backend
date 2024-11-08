from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class AccountSetting(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    theme = models.CharField(max_length=20, choices=[('light', 'Light'), ('dark', 'Dark')], default='light')
    is_subscriber = models.BooleanField(
        _('subscriber status'),
        default=False,
        help_text=_('Indicates whether the user has subscribed to the newsletter'),
    )

    def __str__(self):
        return f'Settings of {self.account.email}'
