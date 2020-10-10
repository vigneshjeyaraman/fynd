from rest_framework import serializers
from apps.movies.models import Movies

class MovieSerializer(serializers.ModelSerializer):
    """Serializer to serialize Movies"""
    class Meta:
        model = Movies
        fields = '__all__'

class ManageMovieSerializer(serializers.ModelSerializer):
    """Serializer to manage add and update of movies"""

    class Meta:
        model = Movies
        fields = ('name', 'imdb_score', 'director', 'popularity', 'genre')

    def create(self, validated_data):
        """Custom create method to add new movie"""

        genre = validated_data.pop('genre')
        movie_obj = Movies.objects.create(**validated_data)
        movie_obj.genre = str(genre)
        movie_obj.save()
        return movie_obj

    def update(self, instance, validated_data):
        """Custom update method to update movie info"""
        
        genre = validated_data.pop('genre')
        movie_obj = Movies.objects.filter(id=instance.id)
        ins = movie_obj.first()
        ins.genre = str(genre)
        ins.save()
        movie_obj.update(**validated_data)
        return movie_obj
    


