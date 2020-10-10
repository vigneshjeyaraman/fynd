import django_filters
from apps.movies.models import Movies

class MovieFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    imdb_score = django_filters.NumberFilter(lookup_expr='exact')
    director = django_filters.CharFilter(lookup_expr='icontains')
    popularity = django_filters.NumberFilter(lookup_expr='exact')
    genre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Movies
        fields = ['name','imdb_score','director','popularity', 'genre']