from rest_framework import serializers

from susi.models import *


class SusiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Susi
        fields = ['name', 'year', 'susi_type']


class SusiScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SusiSchedule
        fields = ['description', 'start_date', 'end_date']

