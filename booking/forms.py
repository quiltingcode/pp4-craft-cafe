from .models import WorkshopBooking
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput


class BookingForm(forms.ModelForm):
    class Meta:
        model = WorkshopBooking
        fields = ('workshop', 'day', 'time', 'places',)

