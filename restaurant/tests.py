"""
REST Framework modules
"""
from rest_framework.test import APITestCase
from rest_framework import status

"""
Django modules
"""
from django.contrib.auth.models import User, Permission

"""
App modules
"""
from restaurant.models import Server, Customer, Item


"""
Fake data
"""
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


class ItemTests(APITestCase):
    url = "/restaurant/item/"
    url_detail = "/restaurant/item/{}/"

    def setUp(self):
        # Create admin user
        self.admin_user = User.objects.create(
            username="admin", email="admin@test.com", password="admin"
        )
        self.admin_user.is_staff = True

        # Create server user
        self.server_user = User.objects.create(
            username="server", email="server@test.com", password="server"
        )
        Server.objects.create(user=self.server_user, name="server", salary=100)

        # Create customer user
        self.customer_user = User.objects.create(
            username="customer", email="customer@test.com", password="customer"
        )
        Customer.objects.create(user=self.customer_user, name="customer")

        # Add fake items
        for item in menu:
            Item.objects.create(name=item["name"], price=item["price"]).save()

    def test_admin_create_item(self):
        """
        Test item creation by admin user (allowed)
        """

        data = {
            "name": "Pudding",
            "price": 500,
        }

        self.client.force_authenticate(self.admin_user)
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_server_create_item(self):
        """
        Test item creation by server user (forbidden)
        """
        data = {
            "name": "Pudding",
            "price": 500,
        }

        self.client.force_authenticate(self.server_user)
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_customer_create_item(self):
        """
        Test item creation by customer user (forbidden)
        """
        data = {
            "name": "Pudding",
            "price": 500,
        }

        self.client.force_authenticate(self.customer_user)
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_all_items(self):
        """
        Test get all items
        """
        item_amount = Item.objects.all().count()
        self.client.force_authenticate(self.admin_user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), item_amount)

    def test_get_item(self):
        """
        Test get one item
        """
        item_data = menu[0]
        item = Item.objects.get(name=item_data["name"])

        self.client.force_authenticate(self.admin_user)
        response = self.client.get(self.url_detail.format(item.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], item_data["name"])
        self.assertEqual(response.data["price"], item_data["price"])

    def test_update_item(self):
        """
        Test update one item
        """
        item_data = menu[0]
        item = Item.objects.get(name=item_data["name"])
        patch_data = {"price": 2000}

        self.client.force_authenticate(self.admin_user)
        response = self.client.patch(
            self.url_detail.format(item.id), patch_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["price"], patch_data["price"])
        self.assertNotEqual(response.data["price"], item_data["price"])

    def test_delete_item(self):
        """
        Test delete one item
        """
        item_data = menu[0]
        item = Item.objects.get(name=item_data["name"])

        self.client.force_authenticate(self.admin_user)
        response = self.client.delete(self.url_detail.format(item.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
