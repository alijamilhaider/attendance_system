from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils import BaseModel


class User(AbstractUser, BaseModel):
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD, REQUIRED_FIELDS = "email", ["username"]

    profile_picture = models.ImageField(upload_to="images/", null=True, blank=True)
