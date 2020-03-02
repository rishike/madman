from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
import json
from django.conf import settings
from django.db import connections
from collections import namedtuple,defaultdict
from django.template.response import SimpleTemplateResponse
from django.core.exceptions import ValidationError
# from django.views.decorators.csrf import csrf_protect


class MapHomeView(TemplateView):
	template_name  = "map/home.html"




def SaveGeoDataIntoDb(request):
	template_name="map/404.html"
	if request.method == 'POST':
		name = request.POST.get('name')
		lat = request.POST.get('latitude')
		lng = request.POST.get('longitude')
		category = request.POST.get('category')
		image = request.POST.get('image')
		web = request.POST.get('weburl')

		if not name or name is None or len(name) > 25:
			return JsonResponse({'success':False,
								'errors':"The name is must be not empty \
									or Less than 25 characters"
								})

		try:
			# with connections['map'].cursor() as cursor:
			# 	cursor.execute("INSERT INTO cdmx_attractions \
			# 	(geom,name,image, web, category)	\
			# 	VALUES (ST_SETSRID(ST_MAKEPoint("+lng+","+lat+"), 4326), %s, %s, %s, %s)", 
			# 	[name,image, web, category]
			# 	)

			return JsonResponse({"success":True})
		except Exception:
			return JsonResponse({"success":False})


	return SimpleTemplateResponse(template_name)


def GeoDataFromDb(request):
	features=[]
	GeoFieldName = namedtuple('fieldName', 'id, name, image, web, geometry')
	with connections['map'].cursor() as cursor:
		cursor.execute("SELECT id, name, image, web, \
		 ST_AsGeoJSON(geom, 5) as geom \
		 FROM cdmx_attractions order by name")
		for row in map(GeoFieldName._make, cursor.fetchall()):
			features.append({
				'type': 'Feature',
				'properties': {k:row.__getattribute__(k) for k in GeoFieldName._fields if k != 'geometry'},
				'geometry':  json.loads(row.geometry)

			})
			

	featureCollection={"type": "FeatureCollection", 'features':features}
	return  JsonResponse(featureCollection, safe=False)

def GeoJsonData(request):
	getFileName=settings.STATICFILES_DIRS[0]+"\\json\\attractdata.geojson"
	with open(getFileName, 'r') as f:
		data = json.loads(f.read())


	return JsonResponse(data, safe=False)


