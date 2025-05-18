from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """

    email = models.EmailField(
        max_length=250,
        unique=True,
        verbose_name="email address",
        help_text="Required. Enter a valid email address.",
    )
    mobile = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="mobile number",
        help_text="Optional. Enter a valid mobile number.",
    )
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="country",
        help_text="Optional. Enter country where you live.",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="avatar",
        help_text="Optional. You can upload your profile picture.",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
