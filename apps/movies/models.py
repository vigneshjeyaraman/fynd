from django.db import models
from apps.users.models import BaseModel


class Movies(BaseModel):
    """Model to keep track of Movie"""
    name = models.CharField(max_length=100)
    imdb_score = models.FloatField()
    director = models.CharField(max_length=100)
    popularity = models.FloatField()
    # since we are using sqllite for ease we have taken it as text field
    # in mysql and postgres we have ListField and ArrayField respectively
    genre = models.TextField() 

