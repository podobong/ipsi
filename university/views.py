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
    대학 목록을 반환하는 API

    ---
    ## `/`
    ## OUTPUT
        - 'name': 대학 이름
        - 'logo': 대학 로고 파일의 이름
        - 'susis':
            - 'year': 학년도
            - 'name': 전형 이름
        - 'susi_major_blocks':
            - 'name': 수시 학과 블록 이름
        - 'jeongsis':
            - 'year': 학년도
            - 'gun': 군
        - 'jeongsi_major_blocks':
            - 'name': 정시 학과 블록 이름
    '''
    def get(self, request):
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)


class UniversitySelect(APIView):
    '''
    입시 일정을 반환하는 API

    ---
    ## `/select/?univ={대학}&sj={수시/정시}&jh={(수시)전형명}&gun={(정시)군}&block={학과블록}`
    ## INPUT
        - &로 구분되는 query parameter (ex: /select/?univ=서울대학교&sj=수시&jh=일반전형&block=의과대학,수의과대학,치의과대학)
        - 'univ': 대학 이름 (ex: 서울대학교)
        - 'sj': 수시 or 정시
        - 'jh': (수시) 전형 이름 (ex: 일반전형)
        - 'gun': (정시) 군 (ex: 가군)
        - 'block': 학과 블록 이름 (ex: 의과대학,수의과대학,치의과대학)
    ## OUTPUT
        - 'description': 일정 이름
        - 'start_date' : 일정 시작 시간
        - 'end_date' : 일정 종료 시간
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
    '''
    여러 입시 일정을 한 번에 반환하는 API

    ---
    ## `/select/?num={대학개수}&univ0={대학0}&sj0={수시/정시0}&jh0={(수시)전형명0}&gun0={(정시)군0}&block0={학과블록0}&univ1={대학1}&sj1={수시/정시1}&jh0={(수시)전형명1}&gun0={(정시)군1}&block0={학과블록1}&...`
    ## INPUT
        - &로 구분되는 query parameter (ex: /selectall/?num=2&univ0=서울대학교&sj0=수시&jh0=일반전형&block0=의과대학,수의과대학,치의과대학&univ1=서울대학교&sj1=정시&gun1=가군&block1=전 학과)
        - 'num': 입력하는 대학의 개수 (ex: 2)
        - 'univ0': 0번째 대학 이름
        - 'sj0': 0번째 수시 or 정시
        - 'jh0': 0번째 (수시) 전형 이름
        - 'gun0': 0번째 (정시) 군
        - 'block0': 0번째 학과 블록 이름
        - ... (num 개수만큼 입력)
    ## OUTPUT
        - 'num': 대학 인덱스
        - 'univ': 대학 이름
        - 'sj': 수시 or 정시
        - 'jh': (수시) 전형 이름
        - 'gun': (정시) 군
        - 'block': 학과 블록 이름
        - 'schedules': 일정 목록
            - 'description': 일정 이름
            - 'start_date' : 일정 시작 시간
            - 'end_date' : 일정 종료 시간
    '''
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
                    'jh': guns[i],
                    'block': blocks[i],
                    'schedules': JeongsiScheduleSerializer(schedules, many=True).data,
                }
       
        return Response(responses)
