from . import views
from django.urls import path
from django.views.generic import TemplateView
from booking.views import WorkshopsView, ProfilePageBookings, ContactPage, EditBooking, DeleteBooking

urlpatterns = [

    path('contact', ContactPage.as_view(), name='contact'),
    path('workshops/', WorkshopsView.as_view(), name='workshops'),
    path('profile-page', ProfilePageBookings.as_view(), name='profile-page'),
    path('edit-booking/<int:pk>', EditBooking.as_view(), name='edit-booking'),
    path('profile-page/<int:pk>/delete', DeleteBooking.as_view(), name='delete-booking'),
]