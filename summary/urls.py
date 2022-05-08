from django.urls import path, include
from .views import showMediumAPI, showLongAPI

urlpatterns = [
    
    path("medium", showMediumAPI),
    path("long", showLongAPI),

]