from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout

from accounts.forms import RegistrationForm, LoginForm, StudentDetailsForm, companyDetailsForm, SocietyDetailsForm
from accounts.models import MyUser, studentData, CompanyData, SoietyData
from accounts.helper_functions import password_check, email_check

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


                try:
                    user_details = studentData.objects.get(id=user.id)
                    login(request, user)
                    return HttpResponseRedirect('/home')
                except ObjectDoesNotExist:
                    account = MyUser.objects.get(id=user.id)
                    account_type = account.get_account_tyoe()
                    return HttpResponseRedirect("complete_registration/" + account_type +"/"+str(user.id))
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
            "action_value_society": "register/society",
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


            # get the ID so i can pass it in the URL to the complete registration page
            user_id = user.id
            return HttpResponseRedirect("/complete_registration/student/" + str(user_id))

        else:
            #todo: change this that it raises username already in use error
            print "form is invalid"
            # todo: add a parameter that tells them, the username or password was incorrect
            return HttpResponseRedirect("/register")



def company_reg(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        form = RegistrationForm(request.POST or None)
        print form

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password2"]

            print email + password

            user = MyUser.objects.create_user(email=email, password=password, userType="company")
            # todo: send out confirmation email

            # get the ID so i can pass it in the URL to the complete registration page
            user_id = user.id
            return HttpResponseRedirect("/complete_registration/company/" + str(user_id))

        else:
            print "form is invalid"
            # todo: add a parameter that tells them, the username or password was incorrect
            return HttpResponseRedirect("/register")


def society_reg(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        form = RegistrationForm(request.POST or None)
        print form

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password2"]

            print email + password

            user = MyUser.objects.create_user(email=email, password=password, userType="society")
            # todo: send out confirmation email

            # get the ID so i can pass it in the URL to the complete registration page
            user_id = user.id
            return HttpResponseRedirect("/complete_registration/society/" + str(user_id))

        else:
            print "form is invalid"
            # todo: add a parameter that tells them, the username or password was incorrect
            return HttpResponseRedirect("/register")


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
            login(request, user)
            return HttpResponseRedirect('/home')
        except ObjectDoesNotExist:

            if user.user_type == 'student':
                form = StudentDetailsForm(request.POST or None)

                if form.is_valid():
                    f_name = form.cleaned_data["first_name"]
                    s_name= form.cleaned_data["surname"]
                    studyCunt = form.cleaned_data["countryOfStudy"]
                    course= form.cleaned_data['course']
                    university = form.cleaned_data['university']

                    studentData.objects.create(id=user, first_name=f_name, surname=s_name,
                                                           countryOfStudy=studyCunt, course=course, university=university)
                    login(request, user)
                    return HttpResponseRedirect("/home")
                # else:
                #     print "form is invalid"
                context = {
                    "form": StudentDetailsForm(),

                }
                return render(request, "student/CompleteStudentRegistration.html", context)

                pass
            else:
                return HttpResponseRedirect('/login')
        except:
            return HttpResponseRedirect("/404")



def complete_company_registration(request, id):
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
            user_details = CompanyData.objects.get(id=id)
            login(request, user)
            return HttpResponseRedirect('/company_home')
        except ObjectDoesNotExist:

            if user.user_type == 'company':

                form = companyDetailsForm(request.POST or None)

                if form.is_valid():
                    print "there"
                    company_name = form.cleaned_data["company_name"]
                    website = form.cleaned_data["company_website"]
                    city = form.cleaned_data["HQ_city"]
                    industry = form.cleaned_data["industry"]

                    CompanyData.objects.create(id=user, Company_name=company_name, company_website=website,
                                               HQ_city=city, description=None, industry=industry)
                    login(request, user)
                    return HttpResponseRedirect("/company_home")
                # else:
                #     print "form is invalid"
                context = {
                    "form": companyDetailsForm(),

                }
                return render(request, "company/completeCompanyregistration.html", context)

                pass
            else:
                return HttpResponseRedirect('/login')
        except:
            return HttpResponseRedirect("/404")


def complete_society_registration(request, id):
    print "hey"
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        print "ho"
        try:
            user = MyUser.objects.get(id=id)

        except ObjectDoesNotExist:
            return HttpResponseRedirect("/register")
        except:
            return HttpResponseRedirect("/login")

        try:
            user_details = SoietyData.objects.get(id=id)
            login(request, user)
            return HttpResponseRedirect('/home')
        except ObjectDoesNotExist:
            print "lets "
            if user.user_type == 'society':
                form = SocietyDetailsForm(request.POST or None)

                if form.is_valid():
                    name = form.cleaned_data['society_name']
                    university = form.cleaned_data['society_university']
                    fb = form.cleaned_data['society_FB']
                    website = form.cleaned_data['society_website']

                    SoietyData.objects.create(id=user, society_name=name, society_university=university,
                                              society_facebook=fb, society_website=website)
                    login(request, user)
                    return HttpResponseRedirect("/society_home")
                # else:
                #     print "form is invalid"
                context = {
                    "form": SocietyDetailsForm(),

                }
                print "go"
                return render(request, "society/completeSocietyRegistration.html", context)
            else:
                return HttpResponseRedirect('/login')
        except:
            return HttpResponseRedirect("/thisisaknownerror")




def logout_call(request):
    logout(request)
    return HttpResponseRedirect('/')



