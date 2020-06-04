from rest_framework import serializers

from university.models import *
from susi.serializers import SusiSerializer
from jeongsi.serializers import JeongsiSerializer


class SusiMajorBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = SusiMajorBlock
        fields = ('name', )


class JeongsiMajorBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeongsiMajorBlock
        fields = ('name', )


class UniversitySerializer(serializers.ModelSerializer):
    susis = SusiSerializer(many=True, read_only=True)
    susi_major_blocks = SusiMajorBlockSerializer(many=True, read_only=True) 
    jeongsis = JeongsiSerializer(many=True, read_only=True) 
    jeongsi_major_blocks = JeongsiMajorBlockSerializer(many=True, read_only=True)

    class Meta:
        model = University
        fields = ('name', 'logo', 'susis', 'susi_major_blocks', 'jeongsis', 'jeongsi_major_blocks')

