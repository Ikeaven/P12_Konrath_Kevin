from django.urls import path
from crm.views import CompanyViewSet, ClientViewSet, ContractViewSet, EventViewSet
from rest_framework.routers import DefaultRouter

from crm.views import (
    ClientFilteredBySales,
    ClientCustomerList,
    ContractListBySales,
    ContractListByClientID,
    ClientFilteredByName,
    ClientFilteredByEmail,
    ContractListByClientName,
    ContractListByClientEmail,
    ContractListByDate,
    ContractListByAmount,
    EventFilteredByClientName,
    EventFilteredByClientEmail,
    EventFilteredByDate,
    # ApiRoot,
)

router = DefaultRouter()
router.register(r"companies", CompanyViewSet, basename="company")
router.register(r"clients", ClientViewSet, basename="client")
router.register(r"contracts", ContractViewSet, basename="contract")
router.register(r"events", EventViewSet, basename="event")

urlpatterns = [
    path(
        "clients/sales/<int:pk>",
        ClientFilteredBySales.as_view(),
        name="client-list-by-sales",
    ),
    path(
        "clients/customer/<int:int>",
        ClientCustomerList.as_view(),
        name="client-is-customer",
    ),
    path(
        "client/name/<str:name>", ClientFilteredByName.as_view(), name="client-by-name"
    ),
    path(
        "client/email/<str:email>",
        ClientFilteredByEmail.as_view(),
        name="client-by-email",
    ),
    path(
        "contracts/seller/<int:pk>",
        ContractListBySales.as_view(),
        name="contract-list-by-sales",
    ),
    path(
        "contracts/client/id/<int:pk>",
        ContractListByClientID.as_view(),
        name="contract-list-by-client-id",
    ),
    path(
        "contracts/client/name/<str:name>",
        ContractListByClientName.as_view(),
        name="contract-list-by-client-name",
    ),
    path(
        "contracts/client/email/<str:email>",
        ContractListByClientEmail.as_view(),
        name="contract-list-by-client-email",
    ),
    path(
        "contracts/date/<str:date>",
        ContractListByDate.as_view(),
        name="contract-list-by-date",
    ),
    path(
        "contracts/amount/<str:operator>/<int:amount>",
        ContractListByAmount.as_view(),
        name="contract-list-by-amount",
    ),
    path(
        "events/client/name/<str:name>",
        EventFilteredByClientName.as_view(),
        name="event-list-by-client-name",
    ),
    path(
        "events/client/email/<str:email>",
        EventFilteredByClientEmail.as_view(),
        name="event-list-by-client-email",
    ),
    path(
        "events/date/<str:date>",
        EventFilteredByDate.as_view(),
        name="event-list-by-date",
    ),
    # path("", ApiRoot.as_view(), name=ApiRoot.name),
]


urlpatterns += router.urls
