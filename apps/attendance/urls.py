from django.urls import path
from .views import attendance_history_view, mark_attendance_view, leave_request_view

urlpatterns = [
    path("attendance_history/", attendance_history_view, name="data"),
    path("mark_attendance/", mark_attendance_view, name="mark_attendance"),
    path("leave_request/", leave_request_view, name="leave_request"),

]
