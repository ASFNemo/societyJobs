from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout

from accounts.forms import RegistrationForm, LoginForm
from accounts.models import MyUser, studentData

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

                #todo: get whether this is a company/ student or society and call the corresponding complete-reg helper function
                return HttpResponseRedirect("/"+next_url)

        context = {
            "form": form
        }
        return render(request, "generalPages/loginpage.html", context)


def register_page(request):


    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        form = RegistrationForm(request.POST or None)
        context = {
            "form": RegistrationForm(),
            "action_value_society": "register/society$",
            "action_value_student": "register/student",
            "action_value_company": "register/company",
            "submit_btn_value": "Register"

        }
        return render(request, "generalPages/register.html", context)


def student_reg(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        form = RegistrationForm(request.POST or None)
        print form

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password2"]

            print email + password

            user = MyUser.objects.create_user(email=email, password=password, userType="student")
            #todo: send out confirmation email


            #todo: redirect to page to complete user profile
            # get the ID so i can pass it in the URL to the complete registration page
            user_id = user.id
            return HttpResponseRedirect("/complete_registration/student/" + user_id)

        else:
            print "form is invalid"
            # todo: add a parameter that tells them, the username or password was incorrect
            return HttpResponseRedirect("/register")



def company_reg(request):
    pass


def society_reg(request):
    pass


def complete_student_registration(request, id):

    # check if the id is the one that matchest to their email:


    # print "in their"
    # print request
    #
    # return HttpResponseRedirect("/")
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        try:
            user = MyUser.objects.get(id=id)

        except ObjectDoesNotExist:
            return HttpResponseRedirect("/register")
        except:
            return HttpResponseRedirect("/login")

        try:
            user_details = studentData.objects.get(id=id)
            HttpResponseRedirect('/home')
        except ObjectDoesNotExist:

            if user.user_type == 'student':
                form = RegistrationForm(request.POST or None)

                if form.is_valid():
                    f_name = form.cleaned_data["first_name"]
                    s_name= form.cleaned_data["surname"]
                    studyCunt = form.cleaned_data["countryOfStudy"]
                    course= form.cleaned_data['course']
                    university = form.cleaned_data['university']

                    this_user_details = studentData.objects.create_user(id=user, first_name=f_name, surname=s_name,
                                                           countryOfStudy=studyCunt, course=course, university=university)

                    login(request, user)
                    return HttpResponseRedirect("/home")
                # else:
                #     print "form is invalid"
                context = {
                    "form": RegistrationForm(),

                }
                return render(request, "studentHomePage.html", context)

                pass
            else:
                return HttpResponseRedirect('/login')
        except:
            return Http404


def complete_company_registration(request, id):
    print "in there"
    HttpResponseRedirect("/")
    pass


def complete_society_registration(request, id):
    print "in here"
    HttpResponseRedirect("/")
    pass



def logout_call(request):
    logout(request)
    return HttpResponseRedirect('/')



