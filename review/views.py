from rest_framework.views import APIView
from rest_framework.response import Response
from review.models import *
from review.serializers import *

class UniversityReview(APIView):
    def get(self, request, univ):
        university = Review.objects.filter(university=univ)
        serializer = ReviewSerializer(university, many=True)
        return Response(serializer.data)