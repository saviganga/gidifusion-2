from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from account.models import Fan, Player, Coach


class FanSignUp(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'DOB']

    @transaction.atomic
    def save(self):
        
        user = super().save(commit=False)
        user.is_fan = True
        user.save()
        fan = Fan.objects.create(profile=user)
        return user


class CoachSignUp(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'DOB']
    
    @transaction.atomic
    def save(self):

        user = super.save(commit=False)
        user.is_coach = True
        user.save()
        coach = Coach.objects.create(profile=user)
        return user


class PlayerSignUpForm(UserCreationForm):

    position = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'position' 'DOB']

    @transaction.atomic
    def save(self):

        user = super.save(commit=False)
        user.is_player = True
        user.save()
        position = self.cleaned_data.get('position')
        player = Player.objects.create(profile=user, position=position)
        