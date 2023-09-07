"""Django modules"""
from django.shortcuts import render
from django.contrib.auth.models import User

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


def get_permission(model, method, user):
    print("👽", method)
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


class ServerList(generics.ListCreateAPIView):
    """
    API endpoint for restaurant workers

    View for GET, POST
    """

    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    permission_classes = [IsAuthenticated, ServerAccessPermission]
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
    permission_classes = [IsAuthenticated, ServerAccessPermission]


"""
------------------------------------
------------ TABLE VIEWS -----------
------------------------------------
"""


class TableList(generics.ListCreateAPIView):
    """
    API endpoint for restaurant tables

    View for GET, POST
    """

    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated, TableAccessPermission]
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
    permission_classes = [IsAuthenticated, TableAccessPermission]


"""
------------------------------------
---------- CUSTOMER VIEWS ----------
------------------------------------
"""


class CustomerList(generics.ListCreateAPIView):
    """
    API endpoint for restaurant clients

    View for GET, POST
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, CustomerAccessPermission]
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
    permission_classes = [IsAuthenticated, CustomerAccessPermission]


"""
------------------------------------
------------ ORDER VIEWS -----------
------------------------------------
"""


class OrderList(generics.ListCreateAPIView):
    """
    API endpoint for orders

    View for GET, POST
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, OrderAccessPermission]
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
    permission_classes = [IsAuthenticated, OrderAccessPermission]


"""
------------------------------------
------------ ITEM VIEWS ------------
------------------------------------
"""


class ItemList(generics.ListCreateAPIView):
    """
    API endpoint for menu items

    View for GET, POST
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated, ItemAccessPermission]
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
    permission_classes = [IsAuthenticated, ItemAccessPermission]


"""
------------------------------------
--------- ORDER_ITEM VIEWS ---------
------------------------------------
"""


class OrderItemList(generics.ListCreateAPIView):
    """
    API endpoint for items linked to orders

    View for GET, POST
    """

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated, OrderItemAccessPermission]
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
    permission_classes = [IsAuthenticated, OrderItemAccessPermission]
