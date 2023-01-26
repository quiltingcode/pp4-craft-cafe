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


class Reservation(models.Model):
    