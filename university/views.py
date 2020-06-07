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
        def error_msg(message):
            return {'detail': message}

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
            serializer = SusiScheduleSerializer(schedules, many=True)
            return Response(serializer.data)
        elif sj == '정시':
            schedules = JeongsiSchedule.objects.filter(Q(jeongsi__university__name=univ) &
                                                       Q(jeongsi__gun=gun) &
                                                       Q(major_block__name=block))
            serializer = JeongsiScheduleSerializer(schedules, many=True)
            return Response(serializer.data)


class UniversitySelectAll(APIView):
    def get(self, request):
        def error_msg(message):
            return {'detail': message}

        # 대학 개수 받고
        num = None
        if 'num' in request.GET:
            num = int(request.GET['num'])
        if not num:
            return Response(error_msg("requires 'num' parameter"))

        # 대학 개수만큼 리스트 원소 미리 생성 (인덱스로 접근하기 위해)
        univs = []
        sjs = []
        jhs = []
        guns = []
        blocks = []

        for i in range(num):
            univs.append(None)
            sjs.append(None)
            jhs.append(None)
            guns.append(None)
            blocks.append(None)

        # 대학 개수만큼 파라미터 받기
        for i in range(num):
            if ('univ' + str(i)) in request.GET:
                univs[i] = request.GET['univ' + str(i)] 
            if ('sj' + str(i)) in request.GET:
                sjs[i] = request.GET['sj' + str(i)]
            if ('jh' + str(i)) in request.GET:
                jhs[i] = request.GET['jh' + str(i)]
            if ('gun' + str(i)) in request.GET:
                guns[i] = request.GET['gun' + str(i)]
            if ('block' + str(i)) in request.GET:
                blocks[i] = request.GET['block' + str(i)]
        
        # 필요한 파라미터가 없을 경우 에러 메시지 출력
        for i in range(num):
            if not univs[i]:
                return Response(error_msg(f"univ {i}: requires 'univ' parameter"))
            if not sjs[i]:
                return Response(error_msg(f"univ {i}: requires 'sj' parameter"))
            if sjs[i] != '수시' and sjs[i] != '정시':
                return Response(error_msg(f"univ {i}: wrong 'sj' parameter: it must be '수시' or '정시'"))
            if sjs[i] == '수시' and not jhs[i]:
                return Response(error_msg(f"univ {i}: sj='수시' requires 'jh' parameter"))
            if sjs[i] == '정시' and not guns[i]:
                return Response(error_msg(f"univ {i}: sj='정시' requires 'gun' parameter"))
            if not blocks[i]:
                return Response(error_msg(f"univ {i}: requires 'block' parameter"))

        # 받은 파라미터로 적절한 스케줄 검색 후 출력
        # 스케줄이 없으면 에러 메시지 출력
        responses = []
        for i in range(num):
            responses.append(None)
        for i in range(num):
            if sjs[i] == '수시':
                schedules = SusiSchedule.objects.filter(Q(susi__university__name=univs[i]) &
                                                        Q(susi__name=jhs[i]) &
                                                        Q(major_block__name=blocks[i]))
                responses[i] = {
                    'num': i,
                    'univ': univs[i],
                    'sj': sjs[i],
                    'jh': jhs[i],
                    'block': blocks[i],
                    'schedules': SusiScheduleSerializer(schedules, many=True).data,
                }
            elif sjs[i] == '정시':
                schedules = JeongsiSchedule.objects.filter(Q(jeongsi__university__name=univs[i]) &
                                                           Q(jeongsi__gun=guns[i]) &
                                                           Q(major_block__name=blocks[i]))
                responses[i] = {
                    'num': i,
                    'univ': univs[i],
                    'sj': sjs[i],
                    'gun': guns[i],
                    'block': blocks[i],
                    'schedules': JeongsiScheduleSerializer(schedules, many=True).data,
                }
       
        return Response(responses)

