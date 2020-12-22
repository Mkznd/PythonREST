from django.db import models
from django.contrib.auth.user import AbstractBaseUser, PermissionsMixin


# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_stuff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Get Full name of the user"""
        return self.name

    def get_short_name(self):
        """Get short name of the user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return seld.email
