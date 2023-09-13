from rest_framework import serializers
from restaurant.models import *


class UserSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class ServerSerializer(serializers.ModelSerializer):
    """Server model serializer"""

    user = UserSerializer()

    class Meta:
        model = Server
        fields = ["id", "user", "name", "salary"]

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class TableSerializer(serializers.ModelSerializer):
    """Table model serializer"""

    server = ServerSerializer()

    class Meta:
        model = Table
        fields = ["id", "number", "server", "status"]

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class CustomerSerializer(serializers.ModelSerializer):
    """Customer model serializer"""

    user = UserSerializer()
    table = TableSerializer()

    class Meta:
        model = Customer
        fields = ["id", "user", "name", "table"]

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class ItemSerializer(serializers.ModelSerializer):
    """Item model serializer"""

    class Meta:
        model = Item
        fields = ["id", "name", "price", "is_available", "image"]

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class OrderSerializer(serializers.ModelSerializer):
    """Order model serializer"""

    table = TableSerializer()
    item = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "table", "status", "item"]

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
