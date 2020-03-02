from django.urls import path,include
from . import views

app_name = 'map'


urlpatterns = [
    path("", views.MapHomeView.as_view() , name="map_home" ),
    path("geojson/", views.GeoJsonData , name="map_data" ),
    path("geodb/", views.GeoDataFromDb),
    path("add_data/", views.SaveGeoDataIntoDb, name="save_data"),
  ]