from django.shortcuts import render, HttpResponseRedirect


def search_job_helper(request, keyword_or_socName):
    if keyword_or_socName[0] == 0 and keyword_or_socName[1] == 0:
        # just show some random jobs
        pass
    elif keyword_or_socName[0] != 0 and keyword_or_socName[1] == 0:
        # show jobs with that keyword
        pass
    elif keyword_or_socName[0] == 0 and keyword_or_socName[1] != 0:
        # show jobs of that society
        pass
    else:
        # show jobs of that society and keywords
        pass
    return render(request, "generalPages/JobSearchPage.html")