from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from university.models import *
from university.serializers import *


class UniversityList(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class CollegeList(APIView):
    def get(self, request, univ_pk):
        colleges = College.objects.filter(university=univ_pk)
        serializer = CollegeSerializer(colleges, many=True)
        return Response(serializer.data)

