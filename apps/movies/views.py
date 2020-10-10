from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.mixins import (ListModelMixin, CreateModelMixin,
                                   UpdateModelMixin, DestroyModelMixin)
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from apps.movies.serializers import MovieSerializer, ManageMovieSerializer
from apps.movies.models import Movies
from pagination import Pagination
from apps.movies.custom_filters import MovieFilter

class ListMovies(viewsets.ReadOnlyModelViewSet):
    """List Movie for both admin and normal user"""
    queryset = Movies.objects.order_by('-updated_at').all()
    serializer_class = MovieSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter
    pagination_class = Pagination
    
    def list(self, request):
        response = super().list(self, request)
        return Response(data=response.data, status=200)

class ManageMovies(CreateModelMixin,
                   UpdateModelMixin,
                   DestroyModelMixin,
                   viewsets.GenericViewSet):
    """View to add new movies"""
    permission_classes = (permissions.IsAdminUser,)
    def create(self, request):
        data = request.data
        serializer = ManageMovieSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={"message": "Movie added"}, status=200)
    
    def update(self, request, movie_id):
        movie_obj = Movies.objects.filter(id=movie_id).first()
        if not movie_obj:
            return Response(data={"message":"Invalid Movie id"}, status=400)
        serializer = ManageMovieSerializer(data=request.data, instance=movie_obj, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={"message": "Movie data updated"}, status=200)
    
    def destroy(self, request, movie_id):
        movie_obj = Movies.objects.filter(id=movie_id).first()
        if not movie_obj:
            return Response(data={"message":"Invalid Movie id"}, status=400)
        movie_obj.delete()
        return Response(data={'message': "Movie deleted successfully"}, status=200)