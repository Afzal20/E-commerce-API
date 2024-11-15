from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default='Anonymous')
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    username = None  # Remove the username field

    USERNAME_FIELD = 'email'  # login with email
    REQUIRED_FIELDS = []  # No required fields for superuser creation

    objects = CustomUserManager()

    # Adding related_name for groups and permissions to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.email


class Profil(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.TextField(default='Description')
    address = models.CharField(max_length=254, default='Address')
    phone = models.CharField(max_length=20, default='Phone')
    NumberOfOrders = models.IntegerField(default=0)
    orders = models.CharField(max_length=50, default="Not ANY ORDRS")

    def __str__(self):
        return f'{self.user.name} Profile'
    
