from django.contrib import admin
from .models import LongSummary, MediumSummary

# Register your models here.
admin.site.register(LongSummary)
admin.site.register(MediumSummary)