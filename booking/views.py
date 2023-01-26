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

        #Get stored data from django session:
        day = request.session.get('day')
        workshop = request.session.get('workshop')
        
        #Only show the time of the day that has not been selected before:
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
        #Loop days you want in the next 21 days:
        today = datetime.now()
        weekdays = []
        for i in range (0, days):
            x = today + timedelta(days=i)
            y = x.strftime('%A')
            if y == 'Monday' or y == 'Saturday' or y == 'Wednesday':
                weekdays.append(x.strftime('%Y-%m-%d'))
        return weekdays
    
    def checkTime(times, day):
        #Only show the time of the day that has not been selected before:
        x = []
        for k in times:
            if Appointment.objects.filter(day=day, time=k).count() < 1:
                x.append(k)
        return x

    def checkEditTime(times, day, id):
        #Only show the time of the day that has not been selected before:
        x = []
        appointment = Appointment.objects.get(pk=id)
        time = appointment.time
        for k in times:
            if Appointment.objects.filter(day=day, time=k).count() < 1 or time == k:
                x.append(k)
        return x