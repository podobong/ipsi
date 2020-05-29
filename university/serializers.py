from rest_framework import serializers

from university.models import *
from susi.serializers import *
from jeongsi.serializers import *


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['name']


class UniversitySerializer(serializers.ModelSerializer):
    susis = SusiSerializer(many=True, read_only=True)
    jeongsis = JeongsiSerializer(many=True, read_only=True)
    majors = MajorSerializer(many=True, read_only=True)

    class Meta:
        model = University
        fields = ['name', 'logo', 'susis', 'jeongsis', 'majors']

