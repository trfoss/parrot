"""
backend/scoreboard/views.py

Views for the scoreboard page

"""
from django.http import JsonResponse
from .models import KattisHandle, KattisScore

# from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Max, Min

def test(request):
	# obj = KattisHandle.objects.first()
	return JsonResponse({"test":"test"}, safe=False)

def scores_week(request):
	# will have to update points to be the difference
	# week_ago = timezone.timedelta(days = 7) - timezone.now()
	week_ago = timezone.timedelta(days = -7) 
	scores = map(
		lambda obj:{
			"id" : obj.id,
			"score" : obj.score
		# }, KattisScore.objects.all().order_by('score').filter(created_at__gte=week_ago))
		}, KattisScore.objects.filter(id = 2))
	return JsonResponse(list(scores), safe=False)