from rest_framework.views import APIView
from rest_framework.response import Response

from suneung.models import *
from suneung.serializers import *


class SuneungList(APIView):
    '''
    수능 및 모의고사 일정을 반환하는 API

    ---
    ## `/suneung/`
    ## OUTPUT
        - 'description': 일정 이름
        - 'start_date' : 일정 시작 시간
        - 'end_date' : 일정 종료 시간
    '''
    def get(self, request):
        schedules = Suneung.objects.all()
        serializer = SuneungSerializer(schedules, many=True)
        return Response(serializer.data)

