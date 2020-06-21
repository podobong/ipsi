from rest_framework.views import APIView
from rest_framework.response import Response

from susi.serializers import *


class SusiScheduleList(APIView):
    serializer_class = NewSusiScheduleSerializer

    def get(self, request):
        schedules = SusiSchedule.objects.all()
        serializer = NewSusiScheduleSerializer(schedules, many=True)
        return Response(serializer.data)
