from rest_framework import serializers
from restaurant.models import *


class UserSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ServerSerializer(serializers.ModelSerializer):
    """Server model serializer"""

    user = UserSerializer()

    class Meta:
        model = Server
        fields = ["id", "user", "name", "salary"]


class TableSerializer(serializers.ModelSerializer):
    """Table model serializer"""

    server = ServerSerializer()

    class Meta:
        model = Table
        fields = ["id", "number", "server", "status"]


class CustomerSerializer(serializers.ModelSerializer):
    """Customer model serializer"""

    user = UserSerializer()
    table = TableSerializer()

    class Meta:
        model = Customer
        fields = ["id", "user", "name", "table"]


class OrderSerializer(serializers.ModelSerializer):
    """Order model serializer"""

    table = TableSerializer()

    class Meta:
        model = Order
        fields = ["id", "table", "status"]


class ItemSerializer(serializers.ModelSerializer):
    """Item model serializer"""

    class Meta:
        model = Item
        fields = ["id", "name", "price"]


class OrderItemSerializer(serializers.ModelSerializer):
    """OrderItem model serializer"""

    order = OrderSerializer()
    item = ItemSerializer()

    class Meta:
        model = OrderItem
        fields = ["id", "order", "item"]
