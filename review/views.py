from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from university.models import University
from review.serializers import ReviewSerializer


class ReviewList(APIView):
    '''
    대학 리뷰 URL 목록을 반환하는 API

    ---
    ## `/review/`
    ## OUTPUT
        - 'name': 대학 이름
        - 'review_url': 대학 리뷰 URL
    '''
    def get(self, request):
        universities = University.objects.all()
        serializer = ReviewSerializer(universities, many=True)
        return Response(serializer.data)


class ReviewDetail(APIView):
    '''
    특정 대학의 리뷰 URL을 반환하는 API

    ---
    ## `/review/<univ>`
    ## OUTPUT
        - 'name': 대학 이름
        - 'review_url': 대학 리뷰 URL
    '''
    def get_object(self, univ):
        try:
            return University.objects.get(name=univ)
        except University.DoesNotExist:
            raise Http404
    def get(self, request, univ):
        university = self.get_object(univ)
        serializer = ReviewSerializer(university)
        return Response(serializer.data)
