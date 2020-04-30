from django.urls import path

from university import views


urlpatterns = [
    path('', views.UniversityList.as_view()),
    path('college/<int:univ_pk>/', views.CollegeList.as_view()),
]
