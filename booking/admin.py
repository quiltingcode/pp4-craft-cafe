from django.contrib import admin
from .models import WorkshopBooking


@admin.register(WorkshopBooking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('user', 'workshop', 'day', 'time', 'created_on', 'places')
    search_fields = ['user', 'workshop', ]
    list_filter = ('approved', 'created_on')
    actions = ['approve_booking']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
