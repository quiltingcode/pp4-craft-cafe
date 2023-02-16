from . import views
from django.urls import path
from django.views.generic import TemplateView
from booking.views import ProfilePageView, ContactPage, EditBooking, DeleteBooking, DeleteAccount, StaffView, AdminApproval

urlpatterns = [

    path('contact', ContactPage.as_view(), name='contact'),
    path('profile-page', ProfilePageView.as_view(), name='profile-page'),
    path('edit-booking/<int:pk>', EditBooking.as_view(), name='edit-booking'),
    path('profile-page/<int:pk>/delete', DeleteBooking.as_view(), name='delete-booking'),
    path('profile-page/<int:pk>/delete/account', DeleteAccount.as_view(), name='delete-account'),
    path('cafe-dashboard', StaffView.as_view(), name='cafe-dashboard'),
    path('approve/<int:id>/booking', views.AdminApproval.as_view(), name='approve-booking'),

]