from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect


from company_app.forms import new_job
from company_app.models import job
from accounts.models import CompanyData


# Create your views here.

@login_required()
def company_home(request):
    return render(request, "company/companyProfilePage.html")

@login_required()
def add_job(request):
    if request.user.user_type == "company":
        # allow the job to be added

        form = new_job(request.POST or None)

        if form.is_valid():
            job_title = form.cleaned_data['job_title']
            job_type = form.cleaned_data['job_type']
            Job_description = form.cleaned_data['Job_description']
            job_city = form.cleaned_data['job_city']
            pay = form.cleaned_data['pay']
            application_email = form.cleaned_data['application_email']

            the_job = job.objects.create(company_ID=CompanyData.objects.get(id=request.user.id),
                                         job_title=job_title, job_type=job_type, job_description=Job_description,
                                         Job_city=job_city, pay=pay, application_email=application_email, active=True)
            return HttpResponseRedirect("/job/"+str(the_job.id))
        # else:
        #     print "form is invalid"
        context = {
            "form": new_job(),
        }
        return render(request, "company/AddJob.html", context)
    else:
        return HttpResponseRedirect('/Thiswilltaketo404Intentianlly')


@login_required()
def job_page(request, id):
    # this will show the page of the job
    return render(request, "company/")
    pass