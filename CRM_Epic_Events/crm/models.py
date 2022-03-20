from datetime import date
from django.conf import settings
from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=250)
    city = models.CharField(max_length=250, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    street_name = models.CharField(max_length=500, blank=True, null=True)
    address_number = models.IntegerField(blank=True, null=True)
    is_customer = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.company_name

    def set_customer_to_true(self):
        Company.objects.filter(pk=self.pk).update(customer=True)


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="clients", on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Contract_Status(models.Model):
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Contract_Status"
        verbose_name_plural = "Contracts_Status"

    def __str__(self) -> str:
        if self.status is False:
            return "Contrat non signé"
        else:
            return "Contrat signé"


class Contract(models.Model):
    sales_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="contracts", on_delete=models.PROTECT
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    contract_status = models.ForeignKey(
        Contract_Status, on_delete=models.PROTECT, default=0
    )
    amount = models.FloatField()
    payment_due = models.DateField()

    def __str__(self) -> str:
        creation_date = date.strftime(self.date_created, "%d-%m-%Y, %H:%M:%S")
        return f"Contrat passé avec : {self.client} à date du {creation_date}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        company = Company.objects.get(pk=self.client.company.pk)
        company.set_customer_to_true()


class Event_Status(models.Model):
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Event_Status"
        verbose_name_plural = "Events_Status"

    def __str__(self) -> str:
        if self.status is False:
            return "L'évenement n'est pas terminé"
        else:
            return "L'événement est terminé"


class Event(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="events",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    event_status = models.ForeignKey(Event_Status, on_delete=models.PROTECT, default=0)
    attendees = models.PositiveIntegerField(null=True, blank=True)
    event_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
