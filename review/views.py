from rest_framework.views import APIView
from rest_framework.response import Response
from review.models import *
from review.serializers import *

class UniversityReview(APIView):
    '''
    각 대학 리뷰 url을 반환하는 API

    ---
    ## `/review/<univ>`
    ## INPUT
        - '/'로 구분되는 path parameter (ex: /review/고려대학교 )
        - univ는 '연세대학교','서울대학교' 처럼 풀네임으로 넣을 것
    ## OUTPUT
        - 'university': 대학교 이름
        - 'url': 해당 대학의 대학백과 리뷰 사이트 url
    '''
    def get(self, request, univ):
        university = Review.objects.filter(university=univ)
        serializer = ReviewSerializer(university, many=True)
        return Response(serializer.data)