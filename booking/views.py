from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import WorkshopBooking
from django.contrib import messages


def contact(request):
    return render(request, "contact.html", {})