from rest_framework import serializers

from university.models import University


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name', 'review_url')

