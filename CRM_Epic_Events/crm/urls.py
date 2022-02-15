from django.urls import path
from crm.views import CompanyViewSet, ClientViewSet, ContractViewSet, EventViewSet
from rest_framework.routers import DefaultRouter

from crm.views import (
    ClientFilteredBySales,
    ClientCustomerList,
    ContractListBySales,
    ContractListByClient,
)

router = DefaultRouter()
router.register(r"company", CompanyViewSet, basename="company")
router.register(r"client", ClientViewSet, basename="client")
router.register(r"contract", ContractViewSet, basename="contract")
router.register(r"event", EventViewSet, basename="event")

urlpatterns = [
    path(
        "clients/sales/<int:pk>",
        ClientFilteredBySales.as_view(),
        name="client-list-by-sales",
    ),
    path(
        "clients/customer/<int:int>",
        ClientCustomerList.as_view(),
        name="client-customer",
    ),
    path(
        "contracts/seller/<int:pk>",
        ContractListBySales.as_view(),
        name="contract-list-by-sales",
    ),
    path(
        "contracts/client/<int:pk>",
        ContractListByClient.as_view(),
        name="contract_list_by_client",
    ),
]


urlpatterns += router.urls
