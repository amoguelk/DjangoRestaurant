"""Django modules"""
from typing import Any
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader

"""REST Framework modules"""
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import UserRateThrottle as BaseUserRateThrottle
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

"""App modules"""
from restaurant.serializers import *
from restaurant.models import *


class HomePageView(TemplateView):
    template_name = "index.html"


class MenuPageView(TemplateView):
    template_name = "menu.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["items"] = Item.objects.all().values()
        return context


"""
------------------------------------
----------- CUSTOM VIEW -----------
------------------------------------
"""


class CustomListCreateAPIView(generics.ListCreateAPIView):
    def filter_queryset(self, queryset):
        # print("\n🪲 queryset before filters:\n", queryset, end="\n\n")
        queryset = super().filter_queryset(queryset)
        # print("\n🪲 queryset after filters:\n", queryset, end="\n\n")
        return queryset

    def paginate_queryset(self, queryset):
        queryset = super().paginate_queryset(queryset)
        # print("\n🪲 queryset after pagination:\n", queryset, end="\n\n")
        return queryset

    def create(self, request, *args, **kwargs):
        print("🪲 create(): request = ", request, "🪲\n")
        return super().create(request, *args, **kwargs)


"""
------------------------------------
----------- PERMISSIONS -----------
------------------------------------
"""


class IsAdmin(IsAdminUser):
    message = "You need to be an admin to perform this action"

    def has_permission(self, request, view):
        return super().has_permission(request, view)


class IsAdminOrIsCustomer(IsAdminUser):
    message = "You need to be an admin or a customer to perform this action"

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)
        try:
            Customer.objects.get(user=user)
            return True
        except Customer.DoesNotExist:
            return super().has_permission(request, view)


class IsAdminOrIsServer(IsAdminUser):
    message = "You need to be an admin or a server to perform this action"

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)
        try:
            Server.objects.get(user=user)
            return True
        except Server.DoesNotExist:
            return super().has_permission(request, view)


class IsServer(permissions.BasePermission):
    message = "You need to be a server to perform this action"

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)
        try:
            Server.objects.get(user=user)
            return True
        except Server.DoesNotExist:
            return False


class IsCustomer(permissions.BasePermission):
    message = "You need to be a customer to perform this action"

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)
        try:
            Customer.objects.get(user=user)
            return True
        except Customer.DoesNotExist:
            return False


"""
------------------------------------
------------ THROTTLING ------------
------------------------------------
"""


class UserRateThrottle(BaseUserRateThrottle):
    """
    Limit request to 10 per minute
    """

    rate = "10/min"


"""
------------------------------------
----------- SERVER VIEWS -----------
------------------------------------
"""


class ServerList(CustomListCreateAPIView):
    """
    API endpoint for restaurant workers

    View for GET, POST
    """

    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    permission_classes = [IsAdmin]
    throttle_classes = [UserRateThrottle]
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name", "user", "salary"]


class ServerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for restaurant workers

    View for GET, PUT, PATCH, DELETE
    """

    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    permission_classes = [IsAdminOrIsServer]


"""
------------------------------------
------------ TABLE VIEWS -----------
------------------------------------
"""


class TableList(CustomListCreateAPIView):
    """
    API endpoint for restaurant tables

    View for GET, POST
    """

    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAdmin]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["status"]
    pagination_class = LimitOffsetPagination
    ordering_fields = ["number", "status", "server__name"]


class TableDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for restaurant tables

    View for GET, PUT, PATCH, DELETE
    """

    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAdminOrIsServer]


"""
------------------------------------
---------- CUSTOMER VIEWS ----------
------------------------------------
"""


class CustomerList(CustomListCreateAPIView):
    """
    API endpoint for restaurant clients

    View for GET, POST
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminOrIsCustomer]
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name", "user", "table"]


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for restaurant clients

    View for GET, PUT, PATCH, DELETE
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdmin]


"""
------------------------------------
------------ ORDER VIEWS -----------
------------------------------------
"""


class OrderList(CustomListCreateAPIView):
    """
    API endpoint for orders

    View for GET, POST
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrIsCustomer]
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["table"]
    filterset_fields = ["table", "status"]


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for orders

    View for GET, PUT, PATCH, DELETE
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


"""
------------------------------------
------------ ITEM VIEWS ------------
------------------------------------
"""


class ItemList(CustomListCreateAPIView):
    """
    API endpoint for menu items

    View for GET, POST
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAdmin]
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["name"]
    ordering_fields = ["name", "price"]
    filterset_fields = ["is_available"]


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for menu items

    View for GET, PUT, PATCH, DELETE
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAdmin]
