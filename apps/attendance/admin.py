from django.contrib import admin

from .models import Attendance, AttendanceCalculations, LeaveRequest


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    ...


@admin.register(AttendanceCalculations)
class AttendanceCalculationsAdmin(admin.ModelAdmin):
    ...


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ["user", "status"]
