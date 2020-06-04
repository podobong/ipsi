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
    '''
    대학교 목록을 반환하는 API

    ---
    ## `/`
    ## OUTPUT
        - 'name': 대학교 이름
        - 'logo': 대학 로고 파일의 이름
        - 'susis':
            - 'name': 전형 이름
            - 'year': 년도
            - 'sysi_type': 수시의 전형 종류
        - 'jeongsis':
            - 'year': 년도
        - 'majors':
            - 'name': 학과 이름
    '''
    def get(self, request):
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)


class UniversitySelect(APIView):
    '''
    입시 일정을 반환하는 API

    ---
    ## `/select/?univ={대학}&type1={수시/정시}&type2={전형}&major={학과}`
    ## INPUT
        - &로 구분되는 query parameter (ex: /select/?univ=서울대학교&type1=수시&type2=일반전형&major=국어국문학과 )
        - 'univ': 대학교 이름 (ex: 서울대학교)
        - 'type1': 수시 or 정시
        - 'type2': 전형 이름 (ex: 일반전형)
        - 'major': 학과 이름 (ex: 국어국문학과)
    ## OUTPUT
        - 'description': 일정 이름
        - 'start_date' : 일정이 시작되는 날짜
        - 'end_date' : 일정이 끝나는 날짜
    '''
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

