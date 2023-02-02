from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .models import WorkshopBooking
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import generic, View
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


class WorkshopsView(TemplateView):
    template_name = 'workshops.html'


class ContactPage(View):

    def get(self, request):
        if request.method == 'POST':
            workshop = request.POST.get('workshop')
            day = request.POST.get('day')
            request.session['day'] = day
            request.session['workshop'] = workshop
        return render(
            request,
            'contact.html',
            {
                "booking_form": BookingForm(),
                "booked": False
            },
        )

    def post(self, request):
        booking = None

        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = User.objects.get(id=request.user.id)
            booking.email = request.user.email
            booking.name = request.user.username
            booking.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Booking request submitted successfully, awaiting approval.')
        else:
            booking_form = BookingForm()
        
        return render(
            request,
            "profile-page.html",
            {
                "booking": booking,
                "approved": False,
                "booked": True
            },
        )


class ProfilePageBookings(generic.ListView):
    def get(self, request):
        model = WorkshopBooking
        bookings = WorkshopBooking.objects.filter(id=self.request.user.id).order_by("-created_on")
        context = {
            'bookings': bookings
        }
        template_name = "profile-page.html"
        paginate_by = 10
        return render(
            request,
            "profile-page.html",
            context
        )

    def edit_booking(request, booking_id):
        booking = get_object_or_404(WorkshopBooking(), id=booking_id)
        if request.method == 'POST':
            form = EditBookingForm(request.POST, instance=booking)
            if form.is_valid():
                form.save()
                return redirect('profile-page')
        form = EditBookingForm(instance=booking)
        context = {
            'form': form
        }
        return render(request, 'profile-page.html', context)
