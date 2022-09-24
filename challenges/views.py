from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january': 'Beat no meat',
    'february': 'Walk for at least 20 minutes',
    'march': 'Learn Django',
    'april': 'Build projects',
    'may': 'Build portfolio',
    'june': 'Ask her out',
    'july': 'Go for retreat',
    'august': 'Apply for internships',
    'september': 'Bond with family and friends',
    'october': 'Go for evangelism',
    'november': 'Prepare for winter',
    'december': 'winter is here!',
}

# Create your views here.

def index(request):
    
    months = list(monthly_challenges.keys())
    return render(request, 'index.html',{
        'months':months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenge.html", {
            "text":challenge_text,
            "month":month,
        })
        
    except:
        raise Http404()
