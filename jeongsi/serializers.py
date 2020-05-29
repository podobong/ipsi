from rest_framework import serializers

from jeongsi.models import *


class JeongsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jeongsi
        fields = ['year']

