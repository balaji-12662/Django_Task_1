from django.urls import path
from .views import *

urlpatterns = [
    path("movies/", MovieListCreateView.as_view(), name="movie-list-create"),       # GET, POST

    path("movies_put/<int:id>/", MovieUpdateView.as_view(), name="movie-update"),  # PUT
    path("movies_delete/<int:id>/", MovieDeleteView.as_view(), name="movie-delete"),  # DELETE
]
