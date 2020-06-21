from django.urls import path
from susi import views


urlpatterns = [
    path('', views.SusiScheduleList.as_view())
]
