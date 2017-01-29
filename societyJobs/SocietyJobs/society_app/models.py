from __future__ import unicode_literals

from django.db import models

from accounts.models import SoietyData, CompanyData

# Create your models here.

class Society_jobs(models.Model):
    society_id = models.OneToOneField(
        SoietyData
    )

    company_id = models.OneToOneField(
        CompanyData
    )
