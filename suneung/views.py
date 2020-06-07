from rest_framework.views import APIView
from rest_framework.response import Response

from suneung.models import *
from suneung.serializers import *


class SuneungList(APIView):
    def get(self, request):
        schedules = Suneung.objects.all()
        serializer = SuneungSerializer(schedules, many=True)
        return Response(serializer.data)

