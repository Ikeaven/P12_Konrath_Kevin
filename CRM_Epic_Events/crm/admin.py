from django.contrib import admin
from .models import Company, Client, Contract, Contract_Status, Event, Event_Status

admin.site.register([Company, Client, Contract, Event])
