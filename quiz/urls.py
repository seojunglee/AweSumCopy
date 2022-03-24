from django.urls import path, include
from .views import showQuiz

urlpatterns = [
    
    path("show/", showQuiz),
]