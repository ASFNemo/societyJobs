"""SocietyJobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from application.views import home, error_404, apply_to_job
from accounts.views import login_page, login, register_company, register_society, register_student, register_page, logout_call

urlpatterns = [
    url(r'^$', home),

    # account URLS
    url(r'^login$', login_page),
    url(r'^register$', register_page),
    url(r'^complete_registration/company$', register_company),
    url(r'^complete_registration/student$', register_student),
    url(r'^complete_registration/society$', register_society),
    url(r'^logout$', logout_call),


    #application URLs
    url(r'^apply$', apply_to_job),

    #admin URLS
    url(r'^admin/', admin.site.urls),

    # 404 -- DO NOT REMOVE
    url(r'^', error_404),
]
