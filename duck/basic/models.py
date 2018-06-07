from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE')


    def __str__(self):
        return self.user.username

# Create your models here.