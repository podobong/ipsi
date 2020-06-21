from rest_framework import serializers

from susi.models import *


class SusiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Susi
        fields = ('year', 'name')


class SusiScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SusiSchedule
        fields = ('description', 'start_date', 'end_date')


class SusiMajorBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = SusiMajorBlock
        fields = ('name', )


class NewSusiScheduleSerializer(serializers.ModelSerializer):
    susi = SusiSerializer()
    major_block = SusiMajorBlockSerializer()

    class Meta:
        model = SusiSchedule
        fields = ('susi', 'major_block', 'description', 'start_date', 'end_date')
