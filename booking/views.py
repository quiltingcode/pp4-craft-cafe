from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .models import WorkshopBooking
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views import generic, View
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from community.models import Post, Comment
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse


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
        time = request.POST.get("time")
        day = request.POST.get('day')
        places = request.POST.get("places")
        booking_form = BookingForm(data=request.POST)

        # split the string by a common separator, reverse the order, and put
        #  it back together again
        day = day.split('-')
        day.reverse()
        day = '-'.join(day)

        # Check all bookings made on that day at that time, then add up the
        # total places reserved already in these existing bookings.
        bookings_made = WorkshopBooking.objects.filter(day=day, time=time)
        places_reserved = 0
        for b in bookings_made:
            places_reserved += int(b.places)

        # If the total number of places reserved on this date and time is
        # greater than or equal to 10, the user will not be able to make the
        #  booking and is redirected back to the booking form to try again.

        if places_reserved + int(places) <= 10:
            if booking_form.is_valid():
                booking = booking_form.save(commit=False)
                booking.user = User.objects.get(id=request.user.id)
                booking.email = request.user.email
                booking.name = request.user.username
                booking.places = places
                booking.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Booking request successful, awaiting approval.')

                return redirect('profile-page')
            else:
                booking_form = BookingForm()
        else:
            messages.add_message(
                request, messages.ERROR,
                'The selected workshop is full. Try a different workshop.')

        return redirect('contact')


class ProfilePageView(ListView):
    model = WorkshopBooking
    template_name = "profile-page.html"

    def get_context_data(self):
        context = super(ProfilePageView, self).get_context_data()
        context['bookings'] = WorkshopBooking.objects.filter(
            user=self.request.user).order_by("-day")
        context['posts'] = Post.objects.filter(
            author=self.request.user).order_by("-created_on")
        context['comments'] = Comment.objects.filter(
            name=self.request.user).order_by("-created_on")

        return context


class EditBooking(SuccessMessageMixin, UpdateView):
    model = WorkshopBooking
    template_name = 'edit-booking.html'
    fields = ['workshop', 'day', 'time', 'places',]

    def form_valid(self, form):
        # Get the form booking data field values
        booking = None
        time = form.cleaned_data.get('time')
        day = form.cleaned_data.get('day')
        places = form.cleaned_data.get('places')

        # Check all bookings made on that day at that time, then add up the
        # total places reserved already in these existing bookings.
        bookings_made = WorkshopBooking.objects.filter(day=day, time=time)
        places_reserved = 0
        for b in bookings_made:
            places_reserved += int(b.places)
        print(places)
        print(places_reserved)
        if places_reserved + int(places) <= 10:
            if form.is_valid():
                edited_booking = form.save(commit=False)
                edited_booking.approved = False
                edited_booking.save()
                messages.success(
                    self.request,
                    'Updated successfully - awaiting re-approval!')
                return redirect('profile-page')
        else:
            messages.error(
                self.request,
                'The selected workshop is full. Try a different workshop.')

        return redirect('profile-page')


class DeleteBooking(DeleteView):
    model = WorkshopBooking
    template_name = 'delete-booking.html'
    success_url = reverse_lazy('profile-page')


class DeleteAccount(DeleteView):
    model = User
    template_name = 'delete-account.html'
    success_url = reverse_lazy('home')


class StaffView(ListView):
    model = WorkshopBooking
    template_name = "cafe-dashboard.html"

    def get_context_data(self):
        context = super(StaffView, self).get_context_data()
        context['bookings'] = WorkshopBooking.objects.all().order_by("-day")
        context['posts'] = Post.objects.all().order_by("-created_on")
        context['comments'] = Comment.objects.all().order_by("-created_on")

        return context


class AdminApproval(UpdateView):

    def post(self, request, id):
        booking = get_object_or_404(WorkshopBooking, id=id)

        if booking.approved:
            booking.approved = False
            booking.save()
            messages.add_message(
                request, messages.SUCCESS, 'Booking Unapproved')
        else:
            booking.approved = True
            booking.save()
            messages.add_message(
                request, messages.SUCCESS, 'Booking approved')
        return redirect('cafe-dashboard')


class AdminEditBooking(UpdateView):
    model = WorkshopBooking
    template_name = 'admin-edit-booking.html'
    fields = ['workshop', 'day', 'time', 'places', 'approved']
    success_url = reverse_lazy('cafe-dashboard')


class AdminDeleteBooking(DeleteView):
    model = WorkshopBooking
    template_name = 'admin-delete-booking.html'
    success_url = reverse_lazy('cafe-dashboard')


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')
