from . import views
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('import-excel', views.importExcel, name='importExcel'),
    path('downloadExcel/<str:sensor_type>', views.downloadExcel, name='downloadExcel'),
    path('get-sensors-by-types', csrf_exempt(views.getSensorsByTypes), name='getSensorsByTypes'),
    path('get-min-max-of-time-stamps', csrf_exempt(views.getMinMaxOfTimeStamps), name='getMinMaxOfTimeStamps'),
    path('getChartData', csrf_exempt(views.getChartData), name='getChartData'),
    path('getMappingChartData', csrf_exempt(views.getMappingChartData), name='getMappingChartData'),

    path('compare', csrf_exempt(views.compare), name='compare'),
    path('getCompareTimeDetails', csrf_exempt(views.getCompareTimeDetails), name='getCompareTimeDetails'),
    path('getCompareChartData', csrf_exempt(views.getCompareChartData), name='getCompareChartData'),

    path('compare-combine', csrf_exempt(views.compareCombine), name='compareCombine'),
    path('getCompareCombineChartData', csrf_exempt(views.getCompareCombineChartData), name='getCompareCombineChartData'),
    
    path('sensor-type-list', views.sensorTypeList, name='sensorTypeList'),
    path('sensor-type-add', views.sensorTypeAdd, name='sensorTypeAdd'),
    path('sensor-type-edit/<int:id>', views.sensorTypeEdit, name='sensorTypeEdit'),
    
    path('sensor-list', views.sensorList, name='sensorList'),
    path('sensor-add', views.sensorAdd, name='sensorAdd'),
    path('sensor-edit/<int:id>', views.sensorEdit, name='sensorEdit'),

    path('section-list', views.sectionList, name='sectionList'),
    path('section-add', views.sectionAdd, name='sectionAdd'),
    path('section-edit/<int:id>', views.sectionEdit, name='sectionEdit'),

    path('section-sensor-mapping-list', views.sectionSensorMappingList, name='sectionSensorMappingList'),
    path('section-sensor-mapping-add', views.sectionSensorMappingAdd, name='sectionSensorMappingAdd'),
]
