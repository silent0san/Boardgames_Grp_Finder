from django.contrib import admin
from .models import Meeting, MeetingUser

# Register your models here.

admin.site.register(Meeting)
admin.site.register(MeetingUser)
