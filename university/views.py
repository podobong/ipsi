from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response

from university.models import *
from university.serializers import *
from susi.models import *
from susi.serializers import *
from jeongsi.models import *
from jeongsi.serializers import *


class UniversityList(APIView):
    def get(self, request):
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)


class UniversitySelect(APIView):
    def get(self, request):
        univ = request.GET['univ']
        type1 = request.GET['type1']
        if 'type2' in request.GET:
            type2 = request.GET['type2']
        major = request.GET['major']
        
        if type1 == '수시':
            detail = SusiDetail.objects.get(Q(susi__university__name=univ) &
                                            Q(susi__name=type2) &
                                            Q(major__name=major))
            schedules = SusiSchedule.objects.filter(susi_detail=detail)
            serializer = SusiScheduleSerializer(schedules, many=True)
            return Response(serializer.data)
        elif type1 == '정시':
            detail = JeongsiDetail.objects.get(Q(jeongsi__university__name=univ) &
                                               Q(major__name=major))
            schedules = JeongsiSchedule.objects.filter(jeongsi_detail=detail)
            serializer = JeongsiScheduleSerializer(schedules, many=True)
            return Response(serializer.data)
        else:
            pass

