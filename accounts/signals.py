from allauth.account.models import EmailAddress
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=EmailAddress)
def set_default_email_flags(sender, instance, created, **kwargs):
    if created:
        if not instance.primary:
            instance.primary = True
        if not instance.verified:
            instance.verified = True
        instance.save()
