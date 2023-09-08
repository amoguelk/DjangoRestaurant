"""Django modules"""
from typing import Any
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

"""REST Framework modules"""
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

"""App modules"""
from restaurant.serializers import *
from restaurant.models import *


def index(request):
    """Main view"""
    return render(request, "index.html")


"""
------------------------------------
----------- CUSTOM VIEW -----------
------------------------------------
"""


class CustomListCreateAPIView(generics.ListCreateAPIView):
    def filter_queryset(self, queryset):
        print("\n👾 queryset before filters:\n", queryset, end="\n\n")
        queryset = super().filter_queryset(queryset)
        print("\n👾 queryset after filters:\n", queryset, end="\n\n")
        return queryset

    def paginate_queryset(self, queryset):
        queryset = super().paginate_queryset(queryset)
        print("\n👾 queryset after pagination:\n", queryset, end="\n\n")
        return queryset


"""
------------------------------------
----------- PERMISSIONS -----------
------------------------------------
"""


def get_permission(model, method, user):
    if method == "GET":
        return user.has_perm(f"view_{model}")
    if method == "POST":
        return user.has_perm(f"add_{model}")
    if method == "PUT" or method == "PATCH":
        return user.has_perm(f"change_{model}")
    if method == "DELETE":
        return user.has_perm(f"delete_{model}")
    return False


class ServerAccessPermission(permissions.BasePermission):
    message = "You do not have the permissions for this action"

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)

        return get_permission("server", request.method, user)


class TableAccessPermission(permissions.BasePermission):
    message = "You do not have the permissions for this action"

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)

        return get_permission("table", request.method, user)


class CustomerAccessPermission(permissions.BasePermission):
    message = "You do not have the permissions for this action"

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)

        return get_permission("customer", request.method, user)


class OrderAccessPermission(permissions.BasePermission):
    message = "You do not have the permissions for this action"

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)

        return get_permission("order", request.method, user)


class ItemAccessPermission(permissions.BasePermission):
    message = "You do not have the permissions for this action"

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)

        return get_permission("item", request.method, user)


class OrderItemAccessPermission(permissions.BasePermission):
    message = "You do not have the permissions for this action"

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)

        return get_permission("orderitem", request.method, user)


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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]


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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]


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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]


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
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["table"]
    filterset_fields = ["table"]


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
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name", "price"]


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for menu items

    View for GET, PUT, PATCH, DELETE
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]


"""
------------------------------------
--------- ORDER_ITEM VIEWS ---------
------------------------------------
"""


class OrderItemList(CustomListCreateAPIView):
    """
    API endpoint for items linked to orders

    View for GET, POST
    """

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["order", "order__table"]
    ordering_fields = ["order", "item"]


class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for items linked to orders

    View for GET, PUT, PATCH, DELETE
    """

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
