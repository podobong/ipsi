from rest_framework.views import APIView
from rest_framework.response import Response

from susi.models import SusiSchedule
from susi.serializers import SusiScheduleSerializer


class SusiScheduleList(APIView):
    def get(self, request):
        schedules = SusiSchedule.objects.all()
        serializer = SusiScheduleSerializer(schedules, many=True)
        return Response(serializer.data)
