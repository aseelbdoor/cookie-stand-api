from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CookieStand

class cookie_standsTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass2"
        )
        testuser2.save()


        test_cookieStand = CookieStand.objects.create(
            location="jordan",
            owner=testuser1,
            description="No des",
            hourly_sales="zero",
            minimum_customers_per_hour=5,
            maximum_customers_per_hour=10,
            average_cookies_per_sale=5,
        )
        test_cookieStand.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")


    def test_CookieStands_model(self):
        cookieStand = CookieStand.objects.get(id=1)
        actual_owner =str (cookieStand.owner)
        actual_location = str(cookieStand.location)
        actual_description = str(cookieStand.description)
        actual_hourly_sales = str(cookieStand.hourly_sales)
        actual_minimum_customers_per_hour=int(cookieStand.minimum_customers_per_hour)
        actual_maximum_customers_per_hour=int(cookieStand.maximum_customers_per_hour)
        actual_average_cookies_per_sale=int(cookieStand.average_cookies_per_sale)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_location, "jordan")
        self.assertEqual(actual_description, "No des")
        self.assertEqual(actual_hourly_sales,"zero")
        self.assertEqual(actual_minimum_customers_per_hour,5)
        self.assertEqual(actual_maximum_customers_per_hour,10)
        self.assertEqual(actual_average_cookies_per_sale,5)
