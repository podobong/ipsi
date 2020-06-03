from rest_framework import serializers
from review.models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['university', 'url']