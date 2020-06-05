from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from university.models import University
from review.serializers import ReviewSerializer


class ReviewList(APIView):
    def get(self, request):
        universities = University.objects.all()
        serializer = ReviewSerializer(universities, many=True)
        return Response(serializer.data)


class ReviewDetail(APIView):
    def get_object(self, univ):
        try:
            return University.objects.get(name=univ)
        except University.DoesNotExist:
            raise Http404

    def get(self, request, univ):
        university = self.get_object(univ)
        serializer = ReviewSerializer(university)
        return Response(serializer.data)

