from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Movies
from .serializers import MoviesSerializer


class MoviesListCreate(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def delete(self, request, *args, **kwargs):
        Movies.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MoviesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    lookup_field = 'pk'
