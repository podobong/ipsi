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
        univ = sj = jh = gun = block = None

        # 파라미터 받고
        if 'univ' in request.GET:
            univ = request.GET['univ']
        if 'sj' in request.GET:
            sj = request.GET['sj']
        if 'jh' in request.GET:
            jh = request.GET['jh']
        if 'gun' in request.GET:
            gun = request.GET['gun']
        if 'block' in request.GET:
            block = request.GET['block']

        # 필요한 파라미터가 없을 경우 처리하고
        if not univ:
            # print message: requires 'univ' parameter
            pass
        if not sj:
            # print message: requires 'sj' parameter
            pass
        if sj == '수시' and not jh:
            # print message: 'susi' requires 'jh' parameter
            pass
        if sj == '정시' and not gun:
            # print message: 'jeongsi' requires 'gun' parameter
            pass
        if not block:
            # print message: requires 'block' parameter
            pass

        # 받은 파라미터로 적절한 스케줄 검색 후 출력
        if sj == '수시':
            schedules = SusiSchedule.objects.filter(Q(susi__university__name=univ) &
                                                    Q(susi__name=jh) &
                                                    Q(major_block__name=block))
            if not schedules:
                # print message: schedule do not exist
                pass
            else:
                serializer = SusiScheduleSerializer(schedules, many=True)
                return Response(serializer.data)
        elif sj == '정시':
            schedules = JeongsiSchedule.objects.filter(Q(jeongsi__university__name=univ) &
                                                       Q(jeongsi__gun=gun) &
                                                       Q(major_block__name=block))
            if not schedules:
                # print message: schedule do not exist
                pass
            else:
                serializer = JeongsiScheduleSerializer(schedules, many=True)
                return Response(serializer.data)
        else:
            # print message: wrong 'sj' parameter: '수시' or '정시'
            pass

