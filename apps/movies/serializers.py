from rest_framework import serializers
from apps.movies.models import Movies

class MovieSerializer(serializers.ModelSerializer):
    """Serializer to serialize Movies"""
    class Meta:
        model = Movies
        fields = '__all__'

class ManageMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('name', 'imdb_score', 'director', 'popularity', 'genre')

    def create(self, validated_data):
        genre = validated_data.pop('genre')
        movie_obj = Movies.objects.create(**validated_data)
        movie_obj.genre = str(genre)
        movie_obj.save()
        return movie_obj

    def update(self, instance, validated_data):
        genre = validated_data.pop('genre')
        movie_obj = Movies.objects.filter(id=instance.id).update(**validated_data)
        instance.genre = str(genre)
        instance.save()
        return movie_obj
    


