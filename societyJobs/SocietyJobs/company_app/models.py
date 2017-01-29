from __future__ import unicode_literals
from datetime import datetime, timedelta
from django.db import models

from accounts.models import CompanyData

# Create your models here.


class job(models.Model):

    company_ID = models.OneToOneField(
        CompanyData,
        null=False
    )

    job_title = models.CharField(
        verbose_name='Job title',
        max_length=255,
        null=False
    )

    job_type = models.CharField(
        verbose_name='job type',
        max_length=255,
        null=False
    )

    job_description = models.CharField(
        verbose_name='company name',
        max_length=5000,
        null=False
    )

    Job_city = models.CharField(
        verbose_name='City, country',
        max_length=255,
        null=False
    )

    pay = models.DecimalField(
        verbose_name="salary",
        max_digits=12,
        decimal_places=2,
        null = True
    )

    application_email = models.CharField(
        verbose_name='email',
        max_length=255,
        null=False
    )

    date_posted = models.DateTimeField(
        auto_now_add=True,
        null=False
    )

    active = models.BooleanField(
        null=False
    )
    active_for = models.IntegerField(default=datetime.now()+timedelta(days=100))
