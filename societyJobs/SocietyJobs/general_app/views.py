from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from student_app.views import customised_student_home

# Create your views here.


def home(request):
    print request.user.is_authenticated()
    return render(request, "generalPages/home.html")


def error_404(request):
    return render(request, "generalPages/404.html")

@login_required()
def profile_home(request):
    # if the account is linked to a student
    customised_student_home
    # if the account is linked to a society



