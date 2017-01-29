from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from student_app.views import customised_student_home
from forms import FollowForm

# Create your views here.


def home(request):
    print request.user.is_authenticated()
    if (request.user.is_authenticated()):
        print request.user.id
        print request.user.user_type
    return render(request, "generalPages/home.html")


def error_404(request):
    return render(request, "generalPages/404.html")

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
                FollowForm.objects.get_or_create(student_id=request.user.id, society_id=id)
        else:
            return HttpResponseRedirect("/login")
    # else:
    #     print "form is invalid"
    context = {
        "form": FollowForm(),

    }
    return render(request, "generalPages/ViewSociety.html", context)




