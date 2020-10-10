from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """
    Core models to save the common properties such as:
        created_at,
        updated_at,
        last_modified_by"""

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated At")

    class Meta:
        """Meta class"""

        abstract = True
        verbose_name = "BaseModel"

class User(AbstractUser, BaseModel):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
