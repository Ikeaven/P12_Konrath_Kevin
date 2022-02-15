# from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from rest_framework.response import Response
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


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing company instance.
    """

    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [
        IsAuthenticated,
        ClientIsAdminOrSalesOwner,
        IsAdminOrSales,
    ]

    def update(self, request, pk, *args, **kwargs):
        company = Company.objects.get(pk=pk)
        self.check_object_permissions(request, company)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, pk, *args, **kwargs):
        company = Company.objects.get(pk=pk)
        self.check_object_permissions(request, company)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, pk, *args, **kwargs):
        company = Company.objects.get(pk=pk)
        self.check_object_permissions(request, company)
        return super().destroy(request, *args, **kwargs)


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
        client = Client.objects.get(pk=pk)
        self.check_object_permissions(request, client)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, pk, *args, **kwargs):
        client = Client.objects.get(pk=pk)
        self.check_object_permissions(request, client)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, pk, *args, **kwargs):
        client = Client.objects.get(pk=pk)
        self.check_object_permissions(request, client)
        return super().destroy(request, *args, **kwargs)


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
            clients = Client.objects.filter(company__customer=True)
        else:
            clients = Client.objects.filter(company__customer=False)
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
        contract = Contract.objects.get(pk=pk)
        self.check_object_permissions(request, contract)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(pk=pk)
        self.check_object_permissions(request, contract)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(pk=pk)
        self.check_object_permissions(request, contract)
        return super().destroy(request, *args, **kwargs)


class ContractListBySales(generics.ListAPIView):
    """
    This view show all contract for a client
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, pk):
        contracts = Contract.objects.filter(sales_contact=pk)
        serializer = ContractSerializer(contracts, many=True)
        return Response(serializer.data)


class ContractListByClient(generics.ListAPIView):
    """
    This view show all contract for a client
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, pk):
        contracts = Contract.objects.filter(client__pk=pk)
        serializer = ContractSerializer(contracts, many=True)
        return Response(serializer.data)


class EventViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing event instance.
    """

    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated, EventIsAdminOrSupportOwner]

    def update(self, request, pk, *args, **kwargs):
        event = Event.objects.get(pk=pk)
        self.check_object_permissions(request, event)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, pk, *args, **kwargs):
        event = Event.objects.get(pk=pk)
        self.check_object_permissions(request, event)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, pk, *args, **kwargs):
        event = Event.objects.get(pk=pk)
        self.check_object_permissions(request, event)
        return super().destroy(request, *args, **kwargs)
