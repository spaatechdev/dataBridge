from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='index'),
    path('import-excel', views.importExcel, name='importExcel'),
    path('downloadExcel/<str:sensor_type>', views.downloadExcel, name='downloadExcel'),
    path('get-sensors-by-types', csrf_exempt(views.getSensorsByTypes), name='getSensorsByTypes'),
    path('getChartData', csrf_exempt(views.getChartData), name='getChartData'),

    path('compare', csrf_exempt(views.compare), name='compare'),
    path('getCompareTimeDetails', csrf_exempt(views.getCompareTimeDetails), name='getCompareTimeDetails'),
    path('getCompareChartData', csrf_exempt(views.getCompareChartData), name='getCompareChartData'),

    path('compare-combine', csrf_exempt(views.compareCombine), name='compareCombine'),
    path('getCompareCombineChartData', csrf_exempt(views.getCompareCombineChartData), name='getCompareCombineChartData')
]
