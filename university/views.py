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
        def error_msg(message):
            return {'error_msg': message}

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

        # 필요한 파라미터가 없을 경우 에러 메시지 출력
        if not univ:
            return Response(error_msg("requires 'univ' parameter"))
        if not sj:
            return Response(error_msg("requires 'sj' parameter"))
        if sj != '수시' and sj != '정시':
            return Response(error_msg("wrong 'sj' parameter: it must be '수시' or '정시'"))
        if sj == '수시' and not jh:
            return Response(error_msg("sj='수시' requires 'jh' parameter"))
        if sj == '정시' and not gun:
            return Response(error_msg("sj='정시' requires 'gun' parameter"))
        if not block:
            return Response(error_msg("requires 'block' parameter"))

        # 받은 파라미터로 적절한 스케줄 검색 후 출력
        # 스케줄이 없으면 에러 메시지 출력
        if sj == '수시':
            schedules = SusiSchedule.objects.filter(Q(susi__university__name=univ) &
                                                    Q(susi__name=jh) &
                                                    Q(major_block__name=block))
            if not schedules:
                return Response(error_msg('schedule do not exist'))
            serializer = SusiScheduleSerializer(schedules, many=True)
            return Response(serializer.data)
        elif sj == '정시':
            schedules = JeongsiSchedule.objects.filter(Q(jeongsi__university__name=univ) &
                                                       Q(jeongsi__gun=gun) &
                                                       Q(major_block__name=block))
            if not schedules:
                return Response(error_msg('schedule do not exist'))
            serializer = JeongsiScheduleSerializer(schedules, many=True)
            return Response(serializer.data)

