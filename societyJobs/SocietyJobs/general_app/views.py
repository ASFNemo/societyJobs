from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from student_app.views import customised_student_home
from forms import FollowForm
from company_app.models import job
from models import Society_follows

# Create your views here.


def home(request):
    print request.user.is_authenticated()
    if request.user.is_authenticated():
        if request.user.user_type == "student":
            #show jobs to do with the societies they have followed
            pass
        else:
            # show just the generic jobs
            pass
    else:
        # show the latest 2 jobs
        pass
    return render(request, "generalPages/home.html")


def error_404(request):
    # return render(request, "generalPages/404.html")
    return render(request, "company/companyProfilePage.html")

@login_required()
def profile_home(request):
    # if the account is linked to a student
    #customised_student_home
    # if the account is linked to a society
    pass


def society_page(request, id):
    form = FollowForm(request.POST or None)

    if form.is_valid():

        if request.user.is_authenticated:

            if request.user.user_type == "student":
                try:
                    follow = Society_follows.objects.get(student_id=request.user.id, society_id=id)
                    follow.delete()
                except ObjectDoesNotExist:
                    Society_follows.objects.get_or_create(student_id=request.user.id, society_id=id)
        else:
            return HttpResponseRedirect("/login")
    # else:
    #     print "form is invalid"
    context = {
        "form": FollowForm(),

    }
    return render(request, "generalPages/ViewSociety.html", context)

def company_page(request, id):
    # work out if we should be able to follow companies or just societies
    # form = FollowForm(request.POST or None)
    #
    # if form.is_valid():
    #
    #     if request.user.is_authenticated:
    #
    #         if request.user.user_type == "student":
    #             FollowForm.objects.get_or_create(student_id=request.user.id, society_id=id)
    #     else:
    #         return HttpResponseRedirect("/login")
    # # else:
    # #     print "form is invalid"
    # context = {
    #     "form": FollowForm(),
    #
    # }

    return render(request, "generalPages/ViewCompany.html")



