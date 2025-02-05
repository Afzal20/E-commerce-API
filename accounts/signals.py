from allauth.account.models import EmailAddress
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUserModel, UserProfile

@receiver(post_save, sender=EmailAddress)
def set_default_email_flags(sender, instance, created, **kwargs):
    if created:
        if not instance.primary:
            instance.primary = True
        if not instance.verified:
            instance.verified = True
            instance.save()


@receiver(post_save, sender=CustomUserModel)
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically creates a UserProfile when a new user is created."""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUserModel)
def save_user_profile(sender, instance, **kwargs):
    """Saves the UserProfile whenever the user is updated."""
    instance.profile.save()
