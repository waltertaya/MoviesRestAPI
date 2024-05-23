from dataclasses import field
from rest_framework import serializers
from .models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'title', 'director', 'release_year']
