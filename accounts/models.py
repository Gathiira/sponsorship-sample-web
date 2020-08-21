from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    is_applicant = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_sponsor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    has_applied = models.BooleanField(default=False)

    def applied(self):
        self.has_applied = True

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

class Sponsor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)



