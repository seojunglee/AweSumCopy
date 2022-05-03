"""awesum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path, include

import summary.views   #앱 이름 summary의 모든 뷰 임포트
import videos.views
from spacy import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', videos.views.index, name="home"),
    path('search/<int:video_id>/', videos.views.searchAPI, name='searchAPI'),
    

    path('quizzes/<int:video_id>/', include('quiz.urls')), #quiz앱의 urls.py 
    path('summaries/<int:video_id>/', include('summary.urls')), #summary앱의 urls.py
    path('subtitles/<int:video_id>/', include('videos.urls')),

    path('videos/', include('videos.urls')),
]