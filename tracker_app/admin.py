from django.contrib import admin
from .models import Status
from .models import Issue
from .models import Feature

# Register your models here.

admin.site.register(Status)
admin.site.register(Issue)
admin.site.register(Feature)