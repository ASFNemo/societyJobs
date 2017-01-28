from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password, userType):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('you must have a password')

        user = self.model(
            email=self.normalize_email(email),
            user_type=userType
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    user_type = models.CharField(
        verbose_name="type of user",
        max_length=50,
        blank=False,
        null=False
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']

    def get_email(self):
        # The user is identified by their email address
        return self.email

    def get_account_tyoe(self):
        return self.user_type

    # def get_short_name(self):
    #     # The user is identified by their email address
    #     return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    #Todo: use this at a later point to allow specific users to use different parts of the applications e.g recuiters to post
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class studentData(models.Model):

    id = models.OneToOneField(
        MyUser,
        primary_key=True,
    )

    first_name = models.CharField(
        verbose_name='student first name',
        max_length=255,
        null=False
    )

    countryOfStudy = models.CharField(
        verbose_name='country of study',
        max_length=255,
        null=False
    )

    surname = models.CharField(
        verbose_name='student first name',
        max_length=255,
        null=False
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )


    course = models.CharField(
        verbose_name='course name',
        max_length=255,
        null=True,
    )
    university = models.CharField(
        verbose_name='university name',
        max_length=255,
        null=True,
    )

    def get_name(self):
        return self.first_name

    def get_email(self):
        return self.email

    def get_userType(self):
        return self.user_type

    def get_course(self):
        return self.course

    def get_university(self):
        return self.university

    def get_country_of_study(self):
        return self.countryOfStudy


class CompanyData(models.Model):
    id = models.OneToOneField(
        MyUser,
        primary_key=True,
    )

    Company_name = models.CharField(
        verbose_name='company name',
        max_length=255,
        null=False
    )

    HQ_city = models.CharField(
        verbose_name='HQ_city',
        max_length=255,
        null=False
    )

    description = models.CharField(
        verbose_name="short company description",
        max_length=5000,
        null=True
    )

    industry = models.CharField(
        verbose_name="company primary industry",
        max_length=255,
        null=False
    )

