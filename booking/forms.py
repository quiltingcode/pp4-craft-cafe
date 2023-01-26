from .models import Comment
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = WorkshopBooking
        fields = ('workshop', 'day', 'time', 'places')