from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required()
def apply_to_job(request):
    print "need to sort out git"
    return render(request, "applytojob.html")

@login_required()
def customised_student_home(request):
    pass
