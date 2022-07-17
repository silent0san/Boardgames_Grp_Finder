from django import forms
from django.forms import ModelForm
from .models import Meeting


class MeetingForm(ModelForm):

    class Meta:
        model = Meeting
        exclude = ('attendees',)
        fields = {'meeting_name', 'game_name', 'meeting_date', 'meeting_hour', 'current_amount_of_players',
                  'wanted_amount_of_players', 'city', 'address', 'zip_code', 'ownership'}
        widgets = {'ownership': forms.HiddenInput()}

    field_order = ['meeting_name', 'game_name', 'meeting_date', 'meeting_hour', 'current_amount_of_players',
                   'wanted_amount_of_players', 'city', 'address', 'zip_code', 'ownership']
