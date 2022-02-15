from django.contrib import admin

# from guardian.admin import GuardedModelAdmin
from .models import Company, Client, Contract, Contract_Status, Event, Event_Status


admin.site.register([Company, Client, Contract, Event])
