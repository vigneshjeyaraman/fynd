"""Test cases for movies APIs"""

import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from apps.movies.models import Movies
from apps.users.models import User

def create_user(client):
    """Helper function to create a dummy user"""
    data = data = {
            "email": "abc@test.com",
            "username": "Slash",
            "password": "gunsnroses"
        }
    response = client.post(
        reverse("signup"),
        data = json.dumps(data),
        content_type="application/json"
    )
    return response

class TestMovies(TestCase):
    """Test class for movies API"""

    def setUp(self):
        """setup method which get called before all the unit tests"""
        
        self.client = APIClient()
        Movies.objects.create(name="Avengers", imdb_score=10.0,
                              director="Anthony Russo", popularity=10.0,
                              genre='["action", "superhero"]')
        token = create_user(self.client).json()['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        
    def test_get_movie(self):
        """test get movie api without authorization header"""

        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.get(
            reverse("get_movies")
        )
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    def test_get_movie_with_authenticated_user(self):
        """test get movie api with authorization header"""
        response = self.client.get(
            reverse("get_movies")
        )
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    def test_create_movie_with_normal_user(self):
        """Test create movie api with token of normal user"""
        data = {
            "name": "Transformers",
            "imdb_score": 8.0,
            "popularity": 8.0,
            "director": "Michael Bay",
            "genre": '["action", "aliens"]'
        }
        response = self.client.post(
            reverse("manage_movie"),
            data = json.dumps(data),
            content_type="application/json"
        )
        assert response.status_code == 403
        assert response.json()['detail'] == "You do not have permission to perform this action."
    
    def test_update_movie_with_normal_user(self):
        """Test update movie api with token of normal user"""
        data = {
            "name": "Transformers",
            "imdb_score": 8.0,
            "popularity": 8.0,
            "director": "Michael Bay",
            "genre": '["action", "aliens"]'
        }
        response = self.client.put(
            reverse("manage_movie") + "1",
            data = json.dumps(data),
            content_type="application/json"
        )
        assert response.status_code == 403
        assert response.json()['detail'] == "You do not have permission to perform this action."
    
    def test_delete_movie_with_normal_user(self):
        """Test delete movie api with token of normal user"""
        response = self.client.delete(
            reverse("manage_movie") + "1",
            content_type="application/json"
        )
        assert response.status_code == 403
        assert response.json()['detail'] == "You do not have permission to perform this action."
    
    def test_create_movie_with_super_user(self):
        """Test create movie api with token of admin user"""
        User.objects.filter(id=1).update(is_staff=True, is_superuser=True)
        data = {
            "name": "Transformers",
            "imdb_score": 8.0,
            "popularity": 8.0,
            "director": "Michael Bay",
            "genre": '["action", "aliens"]'
        }
        response = self.client.post(
            reverse("manage_movie"),
            data = json.dumps(data),
            content_type="application/json"
        )
        assert response.status_code == 200
        assert 'message' in response.json()
    
    def test_update_movie_with_super_user(self):
        """Test update movie api with token of admin user"""
        User.objects.filter(id=1).update(is_staff=True, is_superuser=True)
        data = {
            "name": "Transformers",
            "imdb_score": 8.0,
            "popularity": 8.0,
            "director": "Michael Bay",
            "genre": '["action", "aliens"]'
        }
        response = self.client.put(
            reverse("manage_movie") + "1",
            data = json.dumps(data),
            content_type="application/json"
        )
        assert response.status_code == 200
        assert 'message' in response.json()

    def test_delete_movie_with_super_user(self):
        """Test delete movie api with token of admin user"""
        User.objects.filter(id=1).update(is_staff=True, is_superuser=True)
        response = self.client.delete(
            reverse("manage_movie") + "1",
            content_type="application/json"
        )
        assert response.status_code == 200
        assert 'message' in response.json()
    