from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices


class User(AbstractUser):
    class RoleChoices(TextChoices):
        ADMIN = "admin", "Admin"
        MANAGER = "manager", "Manager"
        ACCOUNTING = "accounting", "Accounting"
        EMPLOYEE = "employee", "Employee"

    phone = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(
        max_length=20, choices=RoleChoices.choices, null=True, blank=True
    )
