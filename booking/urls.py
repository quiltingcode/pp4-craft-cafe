from . import views
from django.urls import path
from django.views.generic import TemplateView
from booking.views import WorkshopsView, ProfilePageBookings, ContactPage, EditBooking

urlpatterns = [

    path('contact', ContactPage.as_view(), name='contact'),
    path('workshops/', WorkshopsView.as_view(), name='workshops'),
    path('profile-page', ProfilePageBookings.as_view(), name='profile-page'),
    path('edit-booking/<int:pk>', EditBooking.as_view(), name='edit-booking'), 
]