from django.urls import path
from review import views


urlpatterns = [
    path('review/<univ>', views.UniversityReview.as_view()),
]
