from django.contrib.auth.models import User
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


def populate():
    # Create servers with their users and tables
    print("Creating servers...")
    for i in range(5):
        # Create user
        user = User.objects.create_user(
            username=users[i]["username"],
            password=users[i]["password"],
            email=users[i]["email"],
        )
        user.first_name = users[i]["first_name"]
        user.last_name = users[i]["last_name"]
        print("\tUser created")
        user.save()

        # Create server
        server = Server(
            user=user, name=f"{user.first_name} {user.last_name}", salary=100000
        )
        print("\tServer created")
        server.save()

        # Create tables (two per server)
        t = Table(number=i + 1, server=server)
        print("\tTable created")
        t.save()
        t = Table(number=i + 6, server=server)
        print("\tTable created")
        t.save()

    # Create customers with their users
    print("Creating customers...")
    for i in range(5, 10):
        # Create user
        user = User.objects.create_user(
            username=users[i]["username"],
            password=users[i]["password"],
            email=users[i]["email"],
        )
        user.first_name = users[i]["first_name"]
        user.last_name = users[i]["last_name"]
        print("\tUser created")
        user.save()

        # Create customer
        customer = Customer(user=user, name=f"{user.first_name} {user.last_name}")
        print("\tCustomer created")
        customer.save()

    # Create menu items
    print("Creating menu items...")
    for item in menu:
        i = Item(name=item["name"], price=item["price"])
        print(f"\tItem {item['name']} created")
        i.save()
