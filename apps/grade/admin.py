from django.contrib import admin

from .models import Grading


@admin.register(Grading)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["grade", "threshold"]
