from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    preferred_currency = models.CharField(max_length=10, default='LKR')
    time_zone = models.CharField(max_length=50, default='UTC')
    notification_preferences = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.user.username}'s Profile"
