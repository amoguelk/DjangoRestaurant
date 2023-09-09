from django.contrib import admin
from restaurant.models import *

"""
------------------------------------
----------- SERVER ADMIN -----------
------------------------------------
"""


class ServerAdmin(admin.ModelAdmin):
    list_display = ["name", "salary"]
    search_fields = ["name"]
    ordering = ["name", "salary"]


admin.site.register(Server, ServerAdmin)

"""
------------------------------------
------------ TABLE ADMIN -----------
------------------------------------
"""


class TableAdmin(admin.ModelAdmin):
    list_display = ["number", "server", "status"]
    ordering = ["number", "server"]
    search_fields = ["status", "server"]
    list_filter = ["status"]
    actions = ["make_empty", "make_occupied"]

    @admin.action(description="Mark selected tables as empty")
    def make_empty(modeladmin, request, queryset):
        queryset.update(status="EMPTY")

    @admin.action(description="Mark selected tables as occupied")
    def make_occupied(modeladmin, request, queryset):
        queryset.update(status="OCCUPIED")


admin.site.register(Table, TableAdmin)

"""
------------------------------------
---------- CUSTOMER ADMIN ----------
------------------------------------
"""


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "table"]
    ordering = ["name", "table"]
    search_fields = ["name"]


admin.site.register(Customer, CustomerAdmin)

"""
------------------------------------
------------ ORDER ADMIN -----------
------------------------------------
"""


class OrderAdmin(admin.ModelAdmin):
    list_display = ["table", "status"]
    ordering = ["table"]
    list_filter = ["status"]
    search_fields = ["item"]
    actions = ["make_in_process", "make_completed", "make_cancelled"]

    @admin.action(description="Mark selected orders as in process")
    def make_in_process(modeladmin, request, queryset):
        queryset.update(status="IN PROCESS")

    @admin.action(description="Mark selected orders as completed")
    def make_completed(modeladmin, request, queryset):
        queryset.update(status="COMPLETED")

    @admin.action(description="Mark selected orders as cancelled")
    def make_cancelled(modeladmin, request, queryset):
        queryset.update(status="CANCELLED")


admin.site.register(Order, OrderAdmin)
"""
------------------------------------
------------ ITEM ADMIN ------------
------------------------------------
"""


class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "is_available"]
    search_fields = ["name"]
    ordering = ["name", "price"]
    list_filter = ["is_available"]


admin.site.register(Item, ItemAdmin)
# ! """
# ! ------------------------------------
# ! --------- ORDER_ITEM ADMIN ---------
# ! ------------------------------------
# ! """


# ! class OrderItemAdmin(admin.ModelAdmin):
# !     list_display = ["order", "item"]
# !     ordering = ["order", "item"]


# ! admin.site.register(OrderItem, OrderItemAdmin)
