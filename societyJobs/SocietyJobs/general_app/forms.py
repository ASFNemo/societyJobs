from django import forms


# this form is here to act as a place holder as all we need from the form is the follow button
class FollowForm(forms.Form):
    pass

class JobSearchForm(forms.Form):
    company_or_jobDesc = forms.CharField()
    society = forms.CharField()
