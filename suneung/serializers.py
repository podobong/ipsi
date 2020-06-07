from rest_framework import serializers

from suneung.models import *


class SuneungSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suneung
        fields = ('description', 'start_date', 'end_date')

