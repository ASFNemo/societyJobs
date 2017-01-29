from __future__ import unicode_literals

from django.db import models

from accounts.models import SoietyData, studentData

# Create your models here.


class Society_follows(models.Model):
    student_id = models.OneToOneField(
        studentData,
    )

    society_id = models.OneToOneField(
        SoietyData,
    )
