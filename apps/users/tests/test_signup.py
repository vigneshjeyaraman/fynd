"""Test cases for signup apis"""
#pylint: disable=import-error, invalid-name

import json
from django.test import TestCase, Client
from django.urls import reverse


class SignUpTest(TestCase):
    """Class to test possible test cases for
    signup API."""

    def setUp(self):
        """Method to initiate few parameters before test cases"""
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
    def test_new_signup(self):
        """Testing signup"""
        assert self.response.status_code == 200
        assert 'password' not in self.response.json()
        assert 'token' in self.response.json()

    def test_existing_signup(self):
        """Signup with existing email"""
        response = self.client.post(
            reverse("signup"),
            data=json.dumps(self.data),
            content_type="application/json"
        )
        assert response.status_code == 400

    def test_missing_username_field_signup(self):
        """signing up with username missing"""
        data = {
            "email": "test@test.com",
            "password": "qwerty@123"
        }
        response = self.client.post(
            reverse("signup"),
            data=json.dumps(data),
            content_type="application/json"
        )
        assert response.status_code == 400
        assert "username" in response.json()

    def test_missing_email_field_signup(self):
        """signing up with missing email"""
        data = {
            "username": "Kirk",
            "password": "qwerty@123"
        }
        response = self.client.post(
            reverse("signup"),
            data=json.dumps(data),
            content_type="application/json"
        )
        assert response.status_code == 400
        assert "email" in response.json()

    def test_missing_password_field_signup(self):
        """signing up with missing password"""
        data = {
            "username": "Kirk",
            "email": "iam@kirk.com"
        }
        response = self.client.post(
            reverse("signup"),
            data=json.dumps(data),
            content_type="application/json"
        )
        assert response.status_code == 400
        assert "password" in response.json()
