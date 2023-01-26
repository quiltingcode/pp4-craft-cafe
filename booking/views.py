from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import WorkshopBooking
from django.contrib import messages


def contact(request):
    return render(request, "contact.html", {})


class BookingView(View):
    def booking(self, request, *args, **kwargs):
        weekdays = validWeekday(32)
        validateWeekdays = isWeekdayValid(weekdays)
        if request.method == 'POST':
            workshop = request.POST.get('workshop')
            day = request.POST.get('day')
            if workshop is None:
                messages.success(request, "Please Select A Workshop!")
                return redirect('booking')

            request.session['day'] = day
            request.session['workshop'] = workshop

            return redirect('bookingSubmit')
        
        return render(request, 'contact.html', {
            'weekdays': weekdays,
            'validateWeekdays': validateWeekdays,
        })