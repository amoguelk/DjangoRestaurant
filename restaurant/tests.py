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
from restaurant.models import Server, Customer


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

    def test_admin_create_item(self):
        """
        Test item creation by admin user (allowed)
        """

        data = {
            "name": "Pudding",
            "price": 500,
        }

        self.client.force_authenticate(self.admin_user)
        print(
            "🪲 ",
            self.admin_user,
            self.admin_user.is_staff,
            self.admin_user.user_permissions.all(),
        )
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

    # def test_server_get_server(self):
    #     """
    #     Test server retrieval
    #     """
    #     expected_data = {
    #         "id": 13,
    #         "user__id": 20,
    #         "user__username": "clarkeH",
    #         "user__email": "clarkeH@entropix.melbourne",
    #         "name": "Clarke Harding",
    #         "salary": 110000,
    #     }
    #     self.client.force_authenticate(self.server_user)
    #     response = self.client.get(self.url_detail.format(expected_data["id"]))
    #     print("🪲 response", response)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data["name"], expected_data["name"])
