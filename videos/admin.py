from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Video)
admin.site.register(Subtitle)



