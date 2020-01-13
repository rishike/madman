from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
import json
from django.conf import settings


class MapHomeView(TemplateView):
	template_name  = "map/map_index.html"


def GeoJsonData(request):
	getFileName=settings.STATICFILES_DIRS[0]+"\\json\\attractdata.geojson"
	with open(getFileName, 'r') as f:
		data = json.loads(f.read())


	return JsonResponse(data, safe=False)
