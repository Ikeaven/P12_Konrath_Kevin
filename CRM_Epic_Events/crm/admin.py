from django.contrib import admin

# from guardian.admin import GuardedModelAdmin
from .models import Company, Client, Contract, Contract_Status, Event, Event_Status


class ClientAdmin(admin.ModelAdmin):
    @admin.display(description="Is_customer")
    def company_is_customer(self, obj):
        return obj.company.is_customer

    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "mobile",
        "company",
        "sales_contact",
        "company_is_customer",
    )
    list_filter = (
        "sales_contact",
        "last_name",
        "email",
        "company__is_customer",
        "company",
    )


class ContractAdmin(admin.ModelAdmin):
    @admin.display(description="Company")
    def contract_company(self, obj):
        return obj.client.company

    list_display = (
        "sales_contact",
        "client",
        "date_created",
        "amount",
        "contract_company",
    )
    list_filter = (
        "sales_contact",
        "client",
        "date_created",
        "amount",
        "client__last_name",
        "client__email",
        "client__id",
    )


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "contract",
        "date_created",
        "support_contact",
        "event_status",
        "attendees",
        "event_date",
    )
    list_filter = (
        "support_contact",
        "event_status",
        "event_date",
        "contract__client__last_name",
        "contract__client__email",
    )


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("company_name", "city", "is_customer")


admin.site.register(Contract, ContractAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Company, CompanyAdmin)
