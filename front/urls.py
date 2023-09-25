from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='index'),
    path('import-excel', views.importExcel, name='importExcel'),
    path('get-sensors-by-types', csrf_exempt(views.getSensorsByTypes), name='getSensorsByTypes'),
    path('getChartData', csrf_exempt(views.getChartData), name='getChartData')
]
