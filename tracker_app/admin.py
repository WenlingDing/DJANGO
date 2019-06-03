from django.contrib import admin
from .models import Status
from .models import Issue
# Register your models here.

admin.site.register(Status)
admin.site.register(Issue)