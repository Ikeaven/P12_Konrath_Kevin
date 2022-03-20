# from django.shortcuts import render

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from crm.permissions import (
    EventIsAdminOrSupportOwner,
    ClientIsAdminOrSalesOwner,
    IsAdminOrSales,
)
from crm.serializers import (
    CompanySerializer,
    ClientSerializer,
    ContractSerializer,
    EventSerializer,
)
from .models import Client, Company, Contract, Event


class CompanyViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing company instance.
    """

    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsAdminOrSales,
    ]

    def update(self, request, pk, *args, **kwargs):
        try:
            company = Company.objects.get(pk=pk)
            self.check_object_permissions(request, company)
            return super().update(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise NotFound(detail="Company not found !")

    def partial_update(self, request, pk, *args, **kwargs):
        try:
            company = Company.objects.get(pk=pk)
            self.check_object_permissions(request, company)
            return super().partial_update(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise NotFound(detail="Company not found !")

    def destroy(self, request, pk, *args, **kwargs):
        try:
            company = Company.objects.get(pk=pk)
            self.check_object_permissions(request, company)
            return super().destroy(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise NotFound(detail="Company not found !")


class ClientViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing client instance.
    """

    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [
        IsAuthenticated,
        ClientIsAdminOrSalesOwner,
        IsAdminOrSales,
    ]

    def update(self, request, pk, *args, **kwargs):
        try:
            client = Client.objects.get(pk=pk)
            self.check_object_permissions(request, client)
            return super().update(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise NotFound(detail="Client not found !")

    def partial_update(self, request, pk, *args, **kwargs):
        try:
            client = Client.objects.get(pk=pk)
            self.check_object_permissions(request, client)
            return super().partial_update(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise NotFound(detail="Client not found !")

    def destroy(self, request, pk, *args, **kwargs):
        try:
            client = Client.objects.get(pk=pk)
            self.check_object_permissions(request, client)
            return super().destroy(request, *args, **kwargs)

        except ObjectDoesNotExist:
            raise NotFound(detail="Client not found !")


class ClientFilteredBySales(generics.ListAPIView):
    """
    A view for view all client of a sales man
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, pk):
        clients = Client.objects.filter(sales_contact__id=pk)
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


class ClientFilteredByName(generics.ListAPIView):
    """
    Filter client by name
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, name):
        client = Client.objects.filter(last_name=name)
        if client.exists():
            serializer = ClientSerializer(client, many=True)
            return Response(serializer.data)
        else:
            raise NotFound(detail="Client not found !")


class ClientFilteredByEmail(generics.ListAPIView):
    """
    Filter client by email
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, email):
        client = Client.objects.filter(email=email)
        if client.exists():
            serializer = ClientSerializer(client, many=True)
            return Response(serializer.data)
        else:
            raise NotFound(detail="Client not found !")


class ClientCustomerList(generics.ListAPIView):
    """
    This view show all customer or not yet, your choice !
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, int):
        # companys = Company.objects.filter(customer=True)
        if int:
            clients = Client.objects.filter(company__is_customer=True)
        else:
            clients = Client.objects.filter(company__is_customer=False)
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


class ContractViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing contract instance.
    """

    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    permission_classes = [
        IsAuthenticated,
        ClientIsAdminOrSalesOwner,
        IsAdminOrSales,
    ]

    def update(self, request, pk, *args, **kwargs):
        try:
            contract = Contract.objects.get(pk=pk)
            self.check_object_permissions(request, contract)
            return super().update(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise NotFound(detail="Contract not found !")

    def partial_update(self, request, pk, *args, **kwargs):
        try:
            contract = Contract.objects.get(pk=pk)
            self.check_object_permissions(request, contract)
            return super().partial_update(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise NotFound(detail="Contract not found !")

    def destroy(self, request, pk, *args, **kwargs):
        try:
            contract = Contract.objects.get(pk=pk)
            self.check_object_permissions(request, contract)
            return super().destroy(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise NotFound(detail="Contract not found !")


class ContractListBySales(generics.ListAPIView):
    """
    This view show all contract for a client
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, pk):
        contracts = Contract.objects.filter(sales_contact=pk)
        if contracts.exists():
            serializer = ContractSerializer(contracts, many=True)
            return Response(serializer.data)
        else:
            raise NotFound(detail="Contract not Found")


class ContractListByClientID(generics.ListAPIView):
    """
    This view show all contract for a client
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, pk):
        contracts = Contract.objects.filter(client__pk=pk)
        if contracts.exists():
            serializer = ContractSerializer(contracts, many=True)
            return Response(serializer.data)
        else:
            raise NotFound(detail="Contract not found !")


class ContractListByClientName(generics.ListAPIView):
    """
    This view show all contract for a client, with his name
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, name):
        contracts = Contract.objects.filter(client__last_name=name)
        if contracts.exists():
            serializer = ContractSerializer(contracts, many=True)
            return Response(serializer.data)
        else:
            raise NotFound(detail="Contract not found !")


class ContractListByClientEmail(generics.ListAPIView):
    """
    This view show all contract for a client, with his email
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, email):
        contracts = Contract.objects.filter(client__email=email)
        if contracts.exists():
            serializer = ContractSerializer(contracts, many=True)
            return Response(serializer.data)
        else:
            raise NotFound(detail="Contract not found !")


class ContractListByDate(generics.ListAPIView):
    """
    This view show all contracts created on a date
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, date):
        contracts = Contract.objects.filter(date_created=date)
        if contracts.exists():
            serializer = ContractSerializer(contracts, many=True)
            return Response(serializer.data)
        else:
            raise NotFound(detail="Contract not found !")


class ContractListByAmount(generics.ListAPIView):
    """
    This view show all contracts created on a date
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, operator, amount):
        if operator == "=":
            contracts = Contract.objects.filter(amount=amount)
        elif operator == "<":
            contracts = Contract.objects.filter(amount__lte=amount)
        elif operator == ">":
            contracts = Contract.objects.filter(amount__gte=amount)
        else:
            raise NotFound(
                detail="It is not a correct operator, you can use '=', '>' or '<' operators only"
            )
        if contracts.exists():
            serializer = ContractSerializer(contracts, many=True)
            return Response(serializer.data)
        else:
            raise NotFound(detail="Contract not found !")


class EventViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing event instance.
    """

    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated, EventIsAdminOrSupportOwner]

    def update(self, request, pk, *args, **kwargs):
        try:
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(request, event)
            return super().update(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise NotFound(detail="Event not found !")

    def partial_update(self, request, pk, *args, **kwargs):
        try:
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(request, event)
            return super().partial_update(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise NotFound(detail="Event not found !")

    def destroy(self, request, pk, *args, **kwargs):
        try:
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(request, event)
            return super().destroy(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise NotFound(detail="Event not found !")


class EventFilteredByClientName(generics.ListAPIView):
    """
    This view show all events of a client, with his last name
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, name):
        event = Event.objects.filter(contract__client__last_name=name)
        if event.exists():
            serializer = EventSerializer(event, many=True)
            return Response(serializer.data)
        else:
            raise NotFound(detail="Event not found !")


class EventFilteredByClientEmail(generics.ListAPIView):
    """
    This view show all events of a client, with his email
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, email):
        event = Event.objects.filter(contract__client__email=email)
        if event.exists():
            serializer = EventSerializer(event, many=True)
            return Response(serializer.data)
        else:
            raise NotFound(detail="Event not found !")


class EventFilteredByDate(generics.ListAPIView):
    """
    This view filter event by date.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, date):
        event = Event.objects.filter(event_date__date=date)
        if event.exists():
            serializer = EventSerializer(event, many=True)
            return Response(serializer.data)
        else:
            raise NotFound(detail="Event not found !")
