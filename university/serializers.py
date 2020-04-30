from rest_framework import serializers

from university.models import *


class UniversitySerializer(serializers.ModelSerializer):
    region = serializers.CharField(source='get_region_display')

    class Meta:
        model = University
        fields = ['name', 'logo', 'region']


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['university', 'name']


class MajorSerializer(serializers.ModelSerializer):
    moonigwa = serializers.CharField(source='get_moonigwa_display')

    class Meta:
        model = Major
        fields = ['college', 'name', 'moonigwa']

