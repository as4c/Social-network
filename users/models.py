from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class Friendship(models.Model):

    STATUS_CHOICES = (
        ('sent', 'Sent'), 
        ('accepted', 'Accepted'), 
        ('rejected', 'Rejected')
    )

    from_user = models.ForeignKey(User, related_name = 'from_friend_set', on_delete = models.CASCADE)

    to_user = models.ForeignKey(User, related_name = 'to_friend_set', on_delete = models.CASCADE)

    status = models.CharField(max_length = 10, choices = STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add = True)

    updated_at = models.DateTimeField(auto_now=True)
