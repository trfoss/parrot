"""
backend/scoreboard/views.py

Views for the scoreboard page

"""
from django.http import JsonResponse
from .models import KattisHandle, KattisScore

from datetime import datetime, timedelta
# from django.utils import timezone
from django.db.models import Max, Min



def test(request):
	return JsonResponse({"test":"test"}, safe=False)

def scores_week(request):
	week_ago = datetime.now() - timedelta(days=7)
	test = datetime.now() - timedelta(days=21) # need a test date that reaches far enough back in our regress.db test data
	query_result = KattisScore.objects.filter(created_at__gte=week_ago).values('kattis_handle').annotate(points=Max('score') - Min('score'))
	# return JsonResponse(list(query_result), safe=False)
	score_diff_list = map(
		lambda obj:{
			"username" : obj['kattis_handle'],
			"points" : obj['points'], 
		}, query_result)
	return JsonResponse(list(score_diff_list), safe=False)