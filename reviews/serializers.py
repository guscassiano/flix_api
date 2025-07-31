from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'movie', 'stars', 'comment']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.movie:
            data['movie_name'] = instance.movie.title
            data['movie'] = instance.movie.title
        return data