from rest_framework import serializers

from susi.models import *


class SusiScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SusiSchedule
        fields = ('id', 'university', 'sj', 'jh', 'block', 'description', 'start_date', 'end_date')
