"""Django modules"""
from django.shortcuts import render

"""REST Framework modules"""
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

"""App modules"""
from restaurant.serializers import *
from restaurant.models import *


def index(request):
    """Main view"""
    return render(request, "index.html")


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
    permission_classes = [IsAdminUser]
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
    permission_classes = [IsAdminUser]


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
    permission_classes = [IsAdminUser]
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
    permission_classes = [IsAdminUser]


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
    permission_classes = [IsAdminUser]
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
    permission_classes = [IsAdminUser]


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
    permission_classes = [IsAdminUser]
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
    permission_classes = [IsAdminUser]


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
    permission_classes = [IsAdminUser]
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
    permission_classes = [IsAdminUser]


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
    permission_classes = [IsAdminUser]
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
    permission_classes = [IsAdminUser]
