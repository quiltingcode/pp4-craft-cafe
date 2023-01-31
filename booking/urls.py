from . import views
from django.urls import path
from django.views.generic import TemplateView
from booking.views import WorkshopsView
from booking.views import ContactPage

urlpatterns = [

    path('contact', ContactPage.as_view(), name='contact'),
    path('workshops/', WorkshopsView.as_view(), name='workshops'),
    # path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    # path('user-panel', views.userPanel, name='userPanel'),
    # path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    # path('user-update-submit/<int:id>', views.userUpdateSubmit, name='userUpdateSubmit'),
    # path('staff-panel', views.staffPanel, name='staffPanel'),
]