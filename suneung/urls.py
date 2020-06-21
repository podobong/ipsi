from django.urls import path

from suneung import views


urlpatterns = [
    path('', views.SuneungList.as_view()),
]
