from .models import WorkshopBooking
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput


class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['day'].required = True

    class Meta:
        model = WorkshopBooking
        fields = ('workshop', 'day', 'time', 'places',)
