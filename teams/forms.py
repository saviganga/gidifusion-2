from django import forms
from django.db import transaction
from django.forms import ModelForm, fields

from teams.models import Team

class TeamSignUpForm(ModelForm):

    class Meta():
        model = Team
        fields = ['email', 'name']

    @transaction.atomic
    def save(self):

        email = self.cleaned_data.get('email')
        name = self.cleaned_data.get('name')
        team = Team.objects.create(email=email, name=name)
        return team