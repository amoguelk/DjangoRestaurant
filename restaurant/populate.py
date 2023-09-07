from django.contrib.auth.models import User, Group, Permission
from restaurant.models import Server, Table, Customer, Item

users = [
    {
        "first_name": "Kay",
        "last_name": "Stout",
        "email": "kayS@grupoli.bharti",
        "username": "kayS",
        "password": "hola123",
    },
    {
        "first_name": "Clarke",
        "last_name": "Harding",
        "email": "clarkeH@entropix.melbourne",
        "username": "clarkeH",
        "password": "hola123",
    },
    {
        "first_name": "Wilder",
        "last_name": "Knight",
        "email": "wilderK@naxdis.casa",
        "username": "wilderK",
        "password": "hola123",
    },
    {
        "first_name": "Parsons",
        "last_name": "Nolan",
        "email": "parsonsN@earthmark.sy",
        "username": "parsonsN",
        "password": "hola123",
    },
    {
        "first_name": "Kirsten",
        "last_name": "Witt",
        "email": "kirstenW@bizmatic.ir",
        "username": "kirstenW",
        "password": "hola123",
    },
    {
        "first_name": "Elsa",
        "last_name": "Carrillo",
        "email": "elsaC@moreganic.accountants",
        "username": "elsaC",
        "password": "hola123",
    },
    {
        "first_name": "Lavonne",
        "last_name": "Burt",
        "email": "lavonneB@premiant.nc",
        "username": "lavonneB",
        "password": "hola123",
    },
    {
        "first_name": "Vilma",
        "last_name": "Garner",
        "email": "vilmaG@uncorp.pizza",
        "username": "vilmaG",
        "password": "hola123",
    },
    {
        "first_name": "Renee",
        "last_name": "Lane",
        "email": "reneeL@permadyne.beer",
        "username": "reneeL",
        "password": "hola123",
    },
    {
        "first_name": "Ellen",
        "last_name": "Watkins",
        "email": "ellenW@sarasonic.ws",
        "username": "ellenW",
        "password": "hola123",
    },
]

menu = [
    {"name": "Garlic Bread", "price": 4.99},
    {"name": "Caprese Salad", "price": 7.99},
    {"name": "Mozzarella Sticks", "price": 6.49},
    {"name": "Chicken Wings", "price": 9.99},
    {"name": "Spaghetti Bolognese", "price": 12.99},
    {"name": "Grilled Salmon", "price": 15.99},
    {"name": "Margherita Pizza", "price": 11.49},
    {"name": "Steak Frites", "price": 18.99},
    {"name": "Tiramisu", "price": 6.99},
    {"name": "Chocolate Lava Cake", "price": 5.99},
    {"name": "Cheesecake", "price": 7.49},
    {"name": "Fruit Sorbet", "price": 4.49},
    {"name": "Soda (Can)", "price": 1.99},
    {"name": "Iced Tea", "price": 2.49},
    {"name": "House Wine (Glass)", "price": 5.99},
    {"name": "Craft Beer", "price": 4.99},
]

server_permissions = [
    "view_customer",
    "view_item",
    "change_order",
    "delete_order",
    "view_order",
    "view_orderitem",
    "view_server",
    "change_table",
    "view_table",
]

customer_permissions = [
    "view_customer",
    "view_item",
    "add_order",
    "change_order",
    "delete_order",
    "view_order",
    "view_table",
]


def populate():
    """
    Creates (or updates) dummy data to test the app
    """
    # Create user groups
    print("Creating groups...")
    server_group, created = Group.objects.get_or_create(name="Server")
    if created:
        for permission in server_permissions:
            server_group.permissions.add(Permission.objects.get(codename=permission))
        print("\tGroup created")
    customer_group, created = Group.objects.get_or_create(name="Customer")
    if created:
        for permission in customer_permissions:
            customer_group.permissions.add(Permission.objects.get(codename=permission))
        print("\tGroup created")
    # Create servers with their users and tables
    print("Creating servers...")
    for i in range(5):
        # Create user
        user, created = User.objects.get_or_create(
            username=users[i]["username"],
            email=users[i]["email"],
        )
        user.set_password(users[i]["password"])
        user.first_name = users[i]["first_name"]
        user.last_name = users[i]["last_name"]
        user.groups.add(server_group)
        print("\tUser created") if created else print("\tUser updated")
        user.save()

        # Create server
        server, created = Server.objects.get_or_create(
            user=user, name=f"{user.first_name} {user.last_name}", salary=100000
        )
        print("\tServer created") if created else print("\tServer updated")
        server.save()

        # Create tables (two per server)
        table, created = Table.objects.get_or_create(number=i + 1, server=server)
        print("\tTable created") if created else print("\tTable updated")
        table.save()
        table, created = Table.objects.get_or_create(number=i + 6, server=server)
        print("\tTable created") if created else print("\tTable updated")
        table.save()

    # Create customers with their users
    print("Creating customers...")
    for i in range(5, 10):
        # Create user
        user, created = User.objects.get_or_create(
            username=users[i]["username"],
            email=users[i]["email"],
        )
        user.set_password(users[i]["password"])
        user.first_name = users[i]["first_name"]
        user.last_name = users[i]["last_name"]
        user.groups.add(customer_group)
        print("\tUser created") if created else print("\tUser updated")
        user.save()

        # Create customer
        customer, created = Customer.objects.get_or_create(
            user=user, name=f"{user.first_name} {user.last_name}"
        )
        print("\tCustomer created") if created else print("\tCustomer updated")
        customer.save()

    # Create menu items
    print("Creating menu items...")
    for itemObj in menu:
        item, created = Item.objects.get_or_create(
            name=itemObj["name"], price=itemObj["price"]
        )
        print("\tItem created") if created else print("\tItem updated")
        item.save()
