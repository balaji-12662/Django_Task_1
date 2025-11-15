from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Movie
from .serializers import MovieSerializer



class MovieListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    # GET /movies
    def get(self, request):
        movie_ids = request.query_params.get('ids')
        if movie_ids:
            try:
                ids = [int(i.strip()) for i in movie_ids.split(',')]
                movies = Movie.objects.filter(id__in=ids, owner=request.user)
            except ValueError:
                return Response({"error": "Invalid ids format"}, status=400)
        else:
            movies = Movie.objects.filter(owner=request.user)

        return Response(MovieSerializer(movies, many=True).data)

    # POST /movies
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class MovieUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        movie = get_object_or_404(Movie, id=id)

        # Check ownership
        if movie.owner != request.user:
            return Response(
                {"error": "You are not allowed to update this movie"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = MovieSerializer(movie, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        movie = get_object_or_404(Movie, id=id)

        # Check ownership
        if movie.owner != request.user:
            return Response(
                {"error": "You are not allowed to delete this movie"},
                status=status.HTTP_403_FORBIDDEN
            )

        movie.delete()
        return Response({"message": "Movie deleted"}, status=status.HTTP_204_NO_CONTENT)


