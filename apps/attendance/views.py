from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .models import Attendance, AttendanceCalculations, LeaveRequest


def attendance_history_view(request):
    attendances = Attendance.objects.filter(user=request.user)
    context = {"attendances": attendances}
    return render(request=request, template_name="attendance_data.html", context=context)


def mark_attendance_view(request):
    if request.method == "GET":
        if user_attendance := Attendance.objects.filter(user=request.user):
            if user_attendance.filter(created_at__day=datetime.now().day):
                return HttpResponse("Attendance has already marked.")
            Attendance.objects.create(user=request.user)
            user_cal = AttendanceCalculations.objects.get(user=request.user)
            user_cal.attendance_count += 1
            user_cal.save()
            return HttpResponse("Attendance has marked.")
        Attendance.objects.create(user=request.user)
        AttendanceCalculations.objects.create(user=request.user, attendance_count=1)
        return HttpResponse("Attendance has marked.")


def leave_request_view(request):
    if request.method == "GET":
        if LeaveRequest.objects.filter(user=request.user, created_at__day=datetime.now().day):
            return HttpResponse("Leave Request for today already created.")
        LeaveRequest.objects.create(user=request.user)
        return HttpResponse("Leave request has been submitted.")
