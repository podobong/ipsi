from django.urls import path

from university import views


urlpatterns = [
    path('', views.UniversityList.as_view()),
    path('select/', views.UniversitySelect.as_view()),
    path('selectall/', views.UniversitySelectAll.as_view()),
]
