from django.db import models
from utils import BaseModel


class Attendance(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.PROTECT)
    grade = models.CharField(max_length=1, null=True, blank=True)


class AttendanceCalculations(BaseModel):
    user = models.OneToOneField("user.User", on_delete=models.PROTECT)
    leave_count = models.IntegerField(default=0, null=True, blank=True)
    attendance_count = models.IntegerField(default=0, null=True, blank=True)
    absent_count = models.IntegerField(default=0, null=True, blank=True)


class LeaveRequest(BaseModel):
    APPROVED, REJECTED, PENDING = "approved", "rejected", "pending"
    status_choices = [
        (APPROVED, "approved"),
        (REJECTED, "rejected"),
        (PENDING, "pending"),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default=PENDING)
    user = models.ForeignKey("user.User", on_delete=models.PROTECT)
