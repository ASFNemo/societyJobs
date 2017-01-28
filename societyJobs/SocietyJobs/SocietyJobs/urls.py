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


from general_app.views import home, error_404
from student_app.views import apply_to_job, customised_student_home
from accounts.views import login_page, complete_company_registration, complete_society_registration, \
    complete_student_registration, register_page, logout_call, student_reg, society_reg, company_reg


urlpatterns = [

    # general_app URLs
    url(r'^$', home),


    # account URLS
    url(r'^login$', login_page),
    url(r'^register$', register_page),
    url(r'^register/student$', student_reg),
    url(r'^register/company$', company_reg),
    url(r'^register/society$', society_reg),
    url(r'^complete_registration/company/(?P<object_id>\d+)$', complete_company_registration),
    url(r'^complete_registration/student/(?P<object_id>\d+)$', complete_student_registration),
    url(r'^complete_registration/society/(?P<object_id>\d+)$', complete_society_registration),
    url(r'^logout$', logout_call),


    # student_app URLS
    url(r'^home$', customised_student_home),
    url(r'^apply$', apply_to_job),

    # Society_app URLS


    #admin URLS
    url(r'^admin/', admin.site.urls),

    # 404 -- DO NOT REMOVE
    url(r'^', error_404),
]
