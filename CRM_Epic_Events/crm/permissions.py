from rest_framework import permissions


class ClientIsAdminOrSalesOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ["list", "retrieve"]:
            return True
        elif view.action == "create":
            if request.user.is_staff:
                return True
            elif request.user.groups.filter(name="Sales").exists():
                return True
            else:
                return False
        else:
            if request.user.is_staff:
                return True
            elif request.user == obj.sales_contact:
                return True
            else:
                return False


class IsAdminOrSales(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ["list", "retrieve"]:
            return True
        elif view.action == "create":
            if request.user.is_staff:
                return True
            elif request.user.groups.filter(name="Sales").exists():
                return True
            else:
                return False
        else:
            return True


class EventIsAdminOrSupportOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ["list", "retrieve"]:
            return True
        elif view.action == "create":
            if request.user.is_staff:
                return True
            elif request.user.groups.filter(name="Sales").exists():
                return True
            else:
                return False
        else:
            if request.user.is_staff:
                return True
            elif request.user == obj.support_contact:
                return True
            elif request.user == obj.contract.sales_contact:
                return True
            else:
                return False
