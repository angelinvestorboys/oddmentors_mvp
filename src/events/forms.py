from django import forms
from .models import LOCATION, Event

class EventCreationForm(forms.ModelForm):

    start_time = forms.CharField (widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'whatever', "label": ('Start Time'), "type":"time"}))
    title = forms.CharField (widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title', "label": ('Title'), "type":"text"}))
    event_date = forms.CharField (widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Date', "label": ('event_date'), "type":"date"}))
    end_time = forms.CharField (widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'end Time', "label": ('End rime'), "type":"time"}))
    duration = forms.CharField (widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Expected duration time', "label": ('duration'), "type":"text"}))
    country = forms.CharField (widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Host country', "label": ('country'), "type":"text"}))
    location = forms.ChoiceField (choices =LOCATION ,widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'location', "label": ('location'), "type":"text"}))

    state = forms.CharField (widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Host state or province', "label": ('state'), "type":"text"}))

    # description = forms.CharField (widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', "label": ('description'), "type":"text"}))




    class Meta:
        model = Event
        fields = (
            "title", "event_date", "start_time", "end_time", "duration", "location", "country", "state", "description",)
