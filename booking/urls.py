from . import views
from django.urls import path

urlpatterns = [
    path('booking', views.booking, name='booking'),
    path("contact/", views.BookingVIew.as_view(), name="contact"),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    # path('user-panel', views.userPanel, name='userPanel'),
    # path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    # path('user-update-submit/<int:id>', views.userUpdateSubmit, name='userUpdateSubmit'),
    # path('staff-panel', views.staffPanel, name='staffPanel'),
]