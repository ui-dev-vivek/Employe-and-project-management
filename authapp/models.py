from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    is_employee=models.BooleanField(default=False)
    is_client=models.BooleanField(default=False)
    # pass
    def __str__(self):
        return self.username