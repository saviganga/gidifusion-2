from django.db import models

from django.contrib.auth.models import AbstractUser
from teams.models import Team
from account.managers import MyUserManager
# Team model form teams app

# Create your models here.

class MyUser(AbstractUser):
    
    username = None
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=11, blank=True)
    DOB = models.DateField(blank=False, null=False)
    is_fan = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'DOB']


class Fan(models.Model):

    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)


class Coach(models.Model):

    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='coach')


class Player(models.Model):

    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    position = models.CharField(max_length=50, null=False, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
