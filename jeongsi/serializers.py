from rest_framework import serializers

from jeongsi.models import *


class JeongsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jeongsi
        fields = ('year', 'gun')


class JeongsiScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeongsiSchedule
        fields = ('description', 'start_date', 'end_date')

