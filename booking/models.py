from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

WORKSHOP_CHOICES = (
    ("All things Wool", "All things Wool"),
    ("Quilting", "Quilting"),
    ("Clothing", "Clothing"),
    ("Home Decor", "Home Decor"),
    ("Textiles", "Textiles"),
    ("Kids Crafts", "Kids Crafts"),
)

TIME_CHOICES = (
    ("4 PM", "4 PM"),
    ("6 PM", "6 PM"),
    ("10AM", "10AM"),
    ("11:30 AM", "11:30 AM"),
)

PLACES_TO_BOOK = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
)


class WorkshopBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    workshop = models.CharField(max_length=50, choices=WORKSHOP_CHOICES, default="All Things Wool")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="4 PM")
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    places = models.CharField(max_length=50, choices=PLACES_TO_BOOK, default="1")
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
