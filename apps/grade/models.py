from django.db import models

from utils import BaseModel

from django.core.validators import RegexValidator

regex_pattern = RegexValidator(r'^[b-zB-Z]*$')


class Grading(BaseModel):
    grade = models.CharField(max_length=1, unique=True, validators=[regex_pattern])
    threshold = models.IntegerField()
