"""
backend/scoreboard/views.py

Views for the scoreboard page

"""
from datetime import datetime, timedelta
from django.utils.timezone import get_current_timezone
from django.http import JsonResponse, HttpResponse
from django.db.models import Max, Min
from .models import KattisScore, KattisHandle

def get_scores(days):
    """
    Return a Json Response with a list of scores which are the diffence
    between our current date and the argument days.
    """

    days_ago = datetime.now(tz=get_current_timezone()) - timedelta(days=days)
    query_result = KattisScore.objects.filter(
        created_at__gte=days_ago
    ).values('kattis_handle__handle').annotate(
        points=Max('score') - Min('score')
    )

    score_diff_list = map(
        lambda obj: {
            "username" : obj['kattis_handle__handle'],
            "points" : obj['points'],
        }, query_result)
    return JsonResponse(list(score_diff_list), safe=False)

def scores_day(request):
    """
    Returns the score difference for each KattisHandle
    for the past day.
    """
    return get_scores(days=1)

def scores_week(request):
    """
    Returns the score difference for each KattisHandle
    for the past week.
    """
    return get_scores(days=7)

def scores_month(request):
    """
    Returns the score difference for each KattisHandle
    for the past month.
    """
    return get_scores(days=30)

def subscribe(request):
    """
    Subscribes a user, allowing for tracking of 
    scores over time.
    """
    username = request.POST.get("username")
    query_set = KattisHandle.objects.filter(
        handle = username
    )
    if(not len(query_set)):# username not in db
        return HttpResponse(status=404)
    try:
        query_set[0].subscribed = True
        query_set[0].save()
        return HttpResponse(status=200) # success
    except:
        return HttpResponse(status=400) # unable to subscribe user