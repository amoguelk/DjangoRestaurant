from django.db import models
from django.contrib.auth.models import User


class Server(models.Model):
    """Represents a restaurant worker"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.name}"


class Table(models.Model):
    """Links clients to their orders and to the server in charge of said orders"""

    STATUS_TYPES = [
        ("EMPTY", "Empty"),
        ("OCCUPIED", "Occupied"),
    ]
    number = models.IntegerField()
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_TYPES, default="EMPTY")

    def __str__(self) -> str:
        return f"Table #{self.number}"


class Customer(models.Model):
    """Represents a restaurant client"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Item(models.Model):
    """Represents an item on the menu"""

    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Order(models.Model):
    """Represents a group of items ordered by a client"""

    STATUS_TYPES = [
        ("IN PROCESS", "In process"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_TYPES, default="IN PROCESS")
    item = models.ManyToManyField(Item, related_name="order_item")
