from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .models import WorkshopBooking
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic, View
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from community.models import Post, Comment


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
        day = request.session.get('day')
        places = request.POST.get("places")
        booking_form = BookingForm(data=request.POST)
        num_bookings = WorkshopBooking.objects.filter(day=day, time=time).count()
        print(num_bookings)
        if num_bookings + int(places) <= 10:
            print(booking_form)
        # if WorkshopBooking.objects.filter(day=day).count() < 1 and WorkshopBooking.objects.filter(time=time).count() < 1 and WorkshopBooking.objects.filter(places=places).count() < 10:
            if booking_form.is_valid():
                print('i am here')
                booking = booking_form.save(commit=False)
                booking.user = User.objects.get(id=request.user.id)
                booking.email = request.user.email
                booking.name = request.user.username
                booking.save()
                print('i am there')
                messages.add_message(
                    request, messages.SUCCESS,
                    'Booking request submitted successfully, awaiting approval.')
            else:
                booking_form = BookingForm()
        else:
            messages.add_message(
                request, messages.SUCCESS,
                'The selected date is full. please try a different session.')  

        return redirect('profile-page')
        #     request,
        #     "profile-page.html",
        #     {
        #         "booking": booking,
        #         "approved": False,
        #         "booked": True
        #     },
        # )


class ProfilePageView(ListView):
    model = WorkshopBooking
    template_name = "profile-page.html"

    def get_context_data(self):
        context = super(ProfilePageView, self).get_context_data()
        context['bookings'] = WorkshopBooking.objects.filter(user=self.request.user).order_by("-day")
        context['posts'] = Post.objects.filter(author=self.request.user).order_by("-created_on")
        context['comments'] = Comment.objects.filter(name=self.request.user).order_by("-created_on")

        return context


class EditBooking(UpdateView):
    model = WorkshopBooking
    template_name = 'edit-booking.html'
    fields = ['workshop', 'day', 'time', 'places',]
    success_url = '/contact/profile-page'

    # def post(self, request, id):
    #     booking = get_object_or_404(WorkshopBooking, id=id)
    #     if booking.approved:
    #         booking.approved = False
    #         booking.save()
    #         messages.add_message(
    #             request, messages.SUCCESS, 'Booking awaiting Re-Approval')


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
