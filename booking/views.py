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


class ProfilePageView(ListView):
    model = WorkshopBooking
    template_name = "profile-page.html"

    def get_queryset(self):
        logged_user = (self.request.user)
        return logged_user

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data()
        context['bookings_list'] = WorkshopBooking.objects.filter(logged_user).order_by("-day")
        context['posts_list'] = Post.objects.filter(logged_user).order_by("-created_on")
        context['comment_list'] = Comment.objects.filter(logged_user).order_by("-created_on")

        return context


class EditBooking(UpdateView):
    model = WorkshopBooking
    template_name = 'edit-booking.html'
    fields = ['workshop', 'day', 'time', 'places',]
    success_url = '/contact/profile-page'


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

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data()
        context['bookings_list'] = WorkshopBooking.objects.all().order_by("-day")
        context['posts_list'] = Post.objects.all().order_by("-created_on")
        context['comment_list'] = Comment.objects.all().order_by("-created_on")

        return context