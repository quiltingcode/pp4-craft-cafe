from . import views
from django.urls import path

urlpatterns = [

    path('contact', views.booking, name='contact'),
    path('workshops', views.WorkshopsView.as_view(), name="workshops"),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    # path('user-panel', views.userPanel, name='userPanel'),
    # path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    # path('user-update-submit/<int:id>', views.userUpdateSubmit, name='userUpdateSubmit'),
    # path('staff-panel', views.staffPanel, name='staffPanel'),
]