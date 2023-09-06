from django.contrib import admin
from restaurant.models import Server, Table, Customer, Order, Item, OrderItem

admin.site.register(Server)
admin.site.register(Table)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(OrderItem)
