from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def company_home(request):
    return render(request, "companyHomePage.html")
