from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from gamestackr.accounts.models import AccountSetting


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_account(sender, instance, created, **kwargs):
    if created:
        AccountSetting.objects.create(account=instance)
