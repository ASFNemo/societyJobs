from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from accounts.forms import RegistrationForm, LoginForm
from accounts.models import MyUser

# Create your views here.

def login_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        form = LoginForm(request.POST or None)
        next_url = request.GET.get('next')

        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print username, password

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/"+next_url)

        context = {
            "form": form
        }
        return render(request, "loginpage.html", context)


def register_page(request):

    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password2"]

        MyUser.objects.create_user( email=email, password=password)
        #todo: send out confirmation email
        #todo: redirect to page to complete user profile

        print email + password

    if request.user.is_authenticated():
        HttpResponseRedirect("/")
    else:
        context = {
            "form": form,
            "action_value": "",
            "submit_btn_value": "Register"

        }
        return render(request, "register.html", context)


def register_student(request):
    print "in their"
    print request

    return HttpResponseRedirect("/")
    pass


def register_company(request):
    print "in there"
    HttpResponseRedirect("/")
    pass


def register_society(request):
    print "in here"
    HttpResponseRedirect("/")
    pass



def logout_call(request):
    logout(request)
    return HttpResponseRedirect('/')



