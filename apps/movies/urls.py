from django.urls import path
from . import views


urlpatterns = [
    path('get_movies/', views.ListMovies.as_view({"get":"list"}), name='get_movies'),
    path('manage_movie/', views.ManageMovies.as_view({"post":"create"}), name='manage_movie'),
    path('manage_movie/<int:movie_id>', views.ManageMovies.as_view({"put":"update",
                                                                    "delete":"destroy"}), name='manage_movie'),
    
]