from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import WorkshopBooking
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import generic, View
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin


class WorkshopsView(TemplateView):
    template_name = 'workshops.html'


def contact(request):
    return render(request, "contact.html", {})


def booking(request):
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
        'booking_form': BookingForm()
    })


def bookingSubmit(request):
    user = request.user
    times = [
        "4 PM", "6 PM", "10 AM", "11:30 AM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    workshop = request.session.get('workshop')

    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service is not None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
                    if WorkshopBooking.objects.filter(day=day).count() < 11:
                        if WorkshopBooking.objects.filter(day=day, time=time).count() < 1:
                        
                            booking_form = BookingForm(data=request.POST)
                            
                            messages.success(request, "Booking Saved!")
                            return redirect('contact')
                        else:
                            messages.success(request, "The Selected Time slot is full!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Workshop!")

    return render(request, 'bookingSubmit.html', {
        'times': hour,
    })


def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if WorkshopBooking.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):

    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Saturday' or y == 'Wednesday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


# Only show the time of the day that has not been selected before:
def checkTime(times, day):

    x = []
    for k in times:
        if WorkshopBooking.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


# Only show the time of the day that has not been selected before:
def checkEditTime(times, day, id):

    x = []
    booking = WorkshopBooking.objects.get(pk=id)
    time = booking.time
    for k in times:
        if WorkshopBooking.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x
