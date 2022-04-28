from django.urls import path, include
from .views import searchAPI

urlpatterns = [
    
    path("search/", searchAPI),

]