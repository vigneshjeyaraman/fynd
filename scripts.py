import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import json
import django
django.setup()
from apps.movies.models import Movies

with open('imdb.json', 'r') as f:
    data = iter(json.loads(f.read()))
    for movie in data:
        genre = movie.pop('genre')
        poplarity = movie.pop('99popularity')
        movie.update({'popularity':poplarity})
        obj = Movies.objects.create(**movie)
        obj.genre = str(genre)
        obj.save()