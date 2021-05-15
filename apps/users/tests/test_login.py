"""Test cases for login apis"""
#pylint: disable=import-error, invalid-name
import json
from django.test import TestCase, Client
from django.urls import reverse


class TestLogin(TestCase):
    """Test class for testing Login APIs"""
    def setUp(self):
        """Setup method get called for every test case"""
        self.client = Client()
        self.data = {
            "email": "abc@test.com",
            "username": "Slash",
            "password": "gunsnroses"
        }
        self.response = self.client.post(
            reverse("signup"),
            data=json.dumps(self.data),
            content_type="application/json"
        )

    def test_login(self):
        """test case to test login API"""
        data = {
            "email": "abc@test.com",
            "password": "gunsnroses"
        }
        response = self.client.post(
            reverse("login"),
            data=json.dumps(data),
            content_type="application/json"
        )
        assert response.status_code == 200
        assert "token" in response.json()
        assert "password" not in response.json()

    def test_invalid_email_login(self):
        """Test case with invalid email"""
        data = {
            "email": "ab@test.com",
            "password": "gunsnroses"
        }
        response = self.client.post(
            reverse("login"),
            data=json.dumps(data),
            content_type="application/json"
        )
        assert response.status_code == 400

    def test_invalid_password_login(self):
        """Test case with invalid password"""
        data = {
            "email": "abc@test.com",
            "password": "avc"
        }
        response = self.client.post(
            reverse("login"),
            data=json.dumps(data),
            content_type="application/json"
        )
        assert response.status_code == 400
