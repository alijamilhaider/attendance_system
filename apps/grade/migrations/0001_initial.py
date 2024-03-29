# Generated by Django 5.0.1 on 2024-01-08 11:47

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grading',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('grade', models.CharField(max_length=1, unique=True, validators=[django.core.validators.RegexValidator('^[b-zB-Z]*$')])),
                ('threshold', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
