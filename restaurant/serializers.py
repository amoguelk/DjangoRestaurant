from django.core.mail import send_mail
from rest_framework import serializers
from restaurant.models import *


class UserSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ServerSerializer(serializers.ModelSerializer):
    """Server model serializer"""

    name = serializers.CharField(max_length=50, read_only=True)

    class Meta:
        model = Server
        fields = ["id", "user", "name", "salary"]

    def create(self, validated_data):
        user = validated_data["user"]
        validated_data["name"] = f"{user.first_name} {user.last_name}"
        return super().create(validated_data)


class TableSerializer(serializers.ModelSerializer):
    """Table model serializer"""

    class Meta:
        model = Table
        fields = ["id", "number", "server", "status"]

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class CustomerSerializer(serializers.ModelSerializer):
    """Customer model serializer"""

    name = serializers.CharField(max_length=50, read_only=True)

    class Meta:
        model = Customer
        fields = ["id", "user", "name", "table"]

    def create(self, validated_data):
        user = validated_data["user"]
        validated_data["name"] = f"{user.first_name} {user.last_name}"
        return super().create(validated_data)


class ItemSerializer(serializers.ModelSerializer):
    """Item model serializer"""

    class Meta:
        model = Item
        fields = ["id", "name", "price", "is_available", "image"]


class OrderSerializer(serializers.ModelSerializer):
    """Order model serializer"""

    class Meta:
        model = Order
        fields = ["id", "table", "status", "item"]

    def order_created_email(self, table, items):
        context = {"table": table, "items": items}
        template = get_template("order_email.html").render(context)

        print("🪲 EMAIL:\n", template, "\n")

        # send_mail(
        #     subject="Order created",
        #     message=None,
        #     from_email="from@example.com",
        #     recipient_list=[user_email],
        #     fail_silently=False,
        #     html_message=template,
        # )

    def save(self, **kwargs):
        valid = self.is_valid()
        if valid:
            table = self.validated_data["table"]
            items = self.validated_data["item"]
            self.order_created_email(table, items)

        return super().save(**kwargs)
