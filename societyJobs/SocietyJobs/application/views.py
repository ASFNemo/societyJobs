from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


def home(request):
    print request.user.is_authenticated()
    return render(request, "home.html")


def error_404(request):
    return render(request, "404.html")


@login_required()
def apply_to_job(request):
    return render(request, "applytojob.html")