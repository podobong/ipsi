from django.urls import path
from review import views


urlpatterns = [
    path('', views.ReviewList.as_view()),
    path('<univ>/', views.ReviewDetail.as_view()),
]
