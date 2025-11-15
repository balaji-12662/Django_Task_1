from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('owner', 'created_at')