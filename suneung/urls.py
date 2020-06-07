from django.urls import path

from suneung import views


urlpatterns = [
    path('suneung/', views.SuneungList.as_view()),
]
