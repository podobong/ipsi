from django.urls import path

from university import views


urlpatterns = [
    path('', views.UniversityList.as_view()),
]
