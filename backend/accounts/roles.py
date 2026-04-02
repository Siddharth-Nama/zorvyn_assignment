from django.db import models

class UserRole(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    ANALYST = 'ANALYST', 'Analyst'
    VIEWER = 'VIEWER', 'Viewer'
