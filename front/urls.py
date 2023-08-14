from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('import-csv', views.importCsv, name='importCsv'),

    path('', views.multipleLineChart, name='index'),

    path('scatter-chart', views.scatterChart, name='scatterChart'),
    path('getScatterChartData', views.getScatterChartData, name='getScatterChartData'),
    
    path('line-chart', views.lineChart, name='lineChart'),
    path('getLineChartData', csrf_exempt(views.getLineChartData), name='getLineChartData'),

    path('multiple-line-chart', views.multipleLineChart, name='multipleLineChart'),
    path('getMultipleLineChartData', csrf_exempt(views.getMultipleLineChartData), name='getMultipleLineChartData')
]
