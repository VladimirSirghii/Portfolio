from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Adaugă related_name pentru a evita conflictele cu modelul auth.User
    groups = models.ManyToManyField(
        'auth.Group', related_name='custom_user_set')
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_set')
    # Alte câmpuri personalizate pentru utilizator

    extra_field = models.CharField(max_length=100)
