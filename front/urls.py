from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='index'),
    path('chart', views.chart, name='chart'),
    # path('getChartData', csrf_exempt(views.getChartData), name='getChartData')
    path('getChartData', views.getChartData, name='getChartData')
]
