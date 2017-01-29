from django import forms

class new_job(forms.Form):
    job_title = forms.CharField()
    job_type = forms.CharField()
    Job_description = forms.CharField(max_length=5000)
    job_city = forms.CharField()
    pay = forms.DecimalField(max_digits=10, decimal_places=2)
    application_email = forms.CharField()
