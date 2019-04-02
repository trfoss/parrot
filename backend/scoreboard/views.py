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
	# will have to update points to be the difference
	# week_ago = timezone.timedelta(days = 7) - timezone.now()
	week_ago = datetime.now() - timedelta(days=7)
	test = datetime.now() - timedelta(days=21)
	# return JsonResponse({"time": week_ago}, safe=False)
	# print(week_ago)

	test = KattisScore.objects.values("kattis_handle").annotate(min=Min('score')).annotate(max=Max('score'))

	# scores = map(
	# 	lambda obj:{
	# 		"handle" : obj.kattis_handle,
	# 		"score" : obj.score, 
	# 		"date" : obj.created_at
	# 	# }, KattisScore.objects.all().order_by('score').filter(created_at__gte=week_ago))
	# 	}, KattisScore.objects.values("kattis_handle"))
	return JsonResponse(list(test), safe=False)