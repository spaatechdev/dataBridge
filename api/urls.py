from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name='api'
urlpatterns = [
    path('sensor-type-list', csrf_exempt(views.sensorTypeList), name='sensorTypeList'),
    path('sensor-type-add', csrf_exempt(views.sensorTypeAdd), name='sensorTypeAdd'),
    path('sensor-type-edit', csrf_exempt(views.sensorTypeEdit), name='sensorTypeEdit'),
    path('sensor-type-delete', csrf_exempt(views.sensorTypeDelete), name='sensorTypeDelete'),

    path('sensor-list', views.sensorList, name='sensorList'),
    path('sensor-add', views.sensorAdd, name='sensorAdd'),
    path('sensor-edit', views.sensorEdit, name='sensorEdit'),
    path('sensor-delete', views.sensorDelete, name='sensorDelete'),

    path('section-list', views.sectionList, name='sectionList'),
    path('section-add', views.sectionAdd, name='sectionAdd'),
    path('section-edit', views.sectionEdit, name='sectionEdit'),
    path('section-delete', views.sectionDelete, name='sectionDelete'),

    path('section-sensor-mapping-list', views.sectionSensorMappingList, name='sectionSensorMappingList'),
    path('section-sensor-mapping-add', views.sectionSensorMappingAdd, name='sectionSensorMappingAdd'),
    path('section-sensor-mapping-delete', views.sectionSensorMappingDelete, name='sectionSensorMappingDelete'),

    path('upload', views.upload, name='upload'),
]