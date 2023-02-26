from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

WORKSHOP_CHOICES = (
    ("All things Wool", "All things Wool"),
    ("Quilting", "Quilting"),
    ("Clothing", "Clothing"),
    ("Home Crafts", "Home Crafts"),
    ("Needlepoint", "Needlepoint"),
    ("Kids Crafts", "Kids Crafts"),
)

TIME_CHOICES = (
    ("4 - 6pm", "4 - 6pm"),
    ("6 - 8pm", "6 - 8 pm"),
    ("10 - 11:30am", "10 - 11:30am"),
    ("11:30am - 1pm", "11:30am - 1pm"),
)

STATUS = ((0, "Draft"), (1, "Published"))

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
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    workshop = models.CharField(
        max_length=50,
        choices=WORKSHOP_CHOICES,
        blank=False,
        verbose_name="Choose which Craft Workshop you wish to attend"
        )
    day = models.DateField(null=True, verbose_name="Desired Workshop Date")
    time = models.CharField(
        max_length=20,
        choices=TIME_CHOICES,
        default="4 - 6pm",
        verbose_name="Desired Workshop Time"
        )
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    places = models.CharField(
        max_length=50,
        choices=PLACES_TO_BOOK,
        default="1",
        verbose_name="Number of places you wish to reserve"
        )
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"

    def get_absolute_url(self):
        return reverse("profile-page", kwargs={"pk": self.pk})

    def number_of_bookings(self):
        return self.booking.approved.count()
