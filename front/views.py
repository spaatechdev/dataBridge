from django.shortcuts import render, redirect
from datetime import datetime
from dataBridge import settings
from django.contrib import messages
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from . import models
import os
import math
import csv
import environ

import environ
env = environ.Env()
environ.Env.read_env()

context = {}
context['project_name'] = env("PROJECT_NAME")
context['client_name'] = env("CLIENT_NAME")

# Create your views here.


def millisToMinutesAndSeconds(millis=None):
    minutes = math.floor(millis / 60000)
    seconds = '{0:.2f}'.format((millis % 60000) / 1000)
    return str(minutes) + ":" + str('0' if float(seconds) < 10 else '') + str(round(float(seconds)))


def importCsv(request):
    if request.method == "POST":
        csv_list = []
        if request.FILES.get('csv_data', None):
            file = request.FILES['csv_data']
            tmpname = str(datetime.now().microsecond) + \
                os.path.splitext(str(file))[1]
            fs = FileSystemStorage(
                settings.MEDIA_ROOT + "csv/", settings.MEDIA_ROOT + "/csv/")
            fs.save(tmpname, file)
            file_name = "csv/" + tmpname

            with open(settings.MEDIA_ROOT + file_name, newline='', mode='r', encoding='ISO-8859-1') as csvfile:
                # reader = csv.DictReader(csvfile)
                reader = csv.reader(csvfile)
                hour_slab = 0
                flag = 0
                for row in reader:
                    if not row[0]:
                        break
                    splitted = row[0].split(":")
                    totalMiliSeconds = int(splitted[0]) * 60000 + int(splitted[1].split(".")[0]) * 1000 + int(splitted[1].split(".")[1])
                    calculated_time = millisToMinutesAndSeconds(totalMiliSeconds)
                    if int(calculated_time.split(":")[0]) == 59:
                        flag = 1
                        # if len(csv_list) > 1000:
                        #     models.CsvData.objects.bulk_create(csv_list)
                        #     csv_list = []
                        #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
                        #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_time="00:"+calculated_time, hour_slab=hour_slab))
                        # else:
                        #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
                        #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_time="00:"+calculated_time, hour_slab=hour_slab))

                    if flag == 1 and int(calculated_time.split(":")[0]) == 0:
                        hour_slab += 1
                        flag = 0
                        # if len(csv_list) > 1000:
                        #     models.CsvData.objects.bulk_create(csv_list)
                        #     csv_list = []
                        #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
                        #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_time="00:"+calculated_time, hour_slab=hour_slab))
                        # else:
                        #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
                        #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_time="00:"+calculated_time, hour_slab=hour_slab))

                    elif flag == 1 and int(calculated_time.split(":")[0]) != 0:
                        hour_slab += 0
                        # if len(csv_list) > 1000:
                        #     models.CsvData.objects.bulk_create(csv_list)
                        #     csv_list = []
                        #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
                        #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_time="00:"+calculated_time, hour_slab=hour_slab))
                        # else:
                        #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
                        #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_time="00:"+calculated_time, hour_slab=hour_slab))

                    if len(csv_list) > 1000:
                        models.CsvData.objects.bulk_create(csv_list)
                        csv_list = []
                        csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
                                        method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_miliseconds=(hour_slab * 60 * 60 * 1000) + totalMiliSeconds, calculated_time="00:"+calculated_time, hour_slab=hour_slab))
                    else:
                        csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
                                        method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_miliseconds=(hour_slab * 60 * 60 * 1000) + totalMiliSeconds, calculated_time="00:"+calculated_time, hour_slab=hour_slab))

                models.CsvData.objects.bulk_create(csv_list)
                csvfile.close()
                os.remove(settings.MEDIA_ROOT + file_name)
            messages.success(request, 'Csv Data Uploaded Successfully.')
            return redirect('index')
    return render(request, 'front/index.html', context)


def scatterChart(request):
    total_hours = models.CsvData.objects.values('hour_slab').distinct()
    context.update({'total_hours': total_hours})
    return render(request, 'front/scatterChart.html', context)


def getScatterChartData(request):
    if request.method == "POST":
        hour = request.POST['hour']
        csv_data = models.CsvData.objects.filter(hour_slab=int(hour))
        categories = [
            field.name for field in csv_data.model._meta.fields if field.name.startswith('method_')]
        method_1_single_data = []
        method_2_single_data = []
        method_3_single_data = []
        method_4_single_data = []
        method_5_single_data = []
        method_6_single_data = []
        method_7_single_data = []
        method_8_single_data = []
        method_9_single_data = []
        method_10_single_data = []
        for row_data in csv_data:
            method_1_single_data.append([0, float(row_data.method_1)])
            method_2_single_data.append([1, float(row_data.method_2)])
            method_3_single_data.append([2, float(row_data.method_3)])
            method_4_single_data.append([3, float(row_data.method_4)])
            method_5_single_data.append([4, float(row_data.method_5)])
            method_6_single_data.append([5, float(row_data.method_6)])
            method_7_single_data.append([6, float(row_data.method_7)])
            method_8_single_data.append([7, float(row_data.method_8)])
            method_9_single_data.append([8, float(row_data.method_9)])
            method_10_single_data.append([9, float(row_data.method_10)])
        series = [{'name': 'method_1', 'data': method_1_single_data}, {'name': 'method_2', 'data': method_2_single_data}, {'name': 'method_3', 'data': method_3_single_data}, {'name': 'method_4', 'data': method_4_single_data}, {'name': 'method_5', 'data': method_5_single_data}, {
            'name': 'method_6', 'data': method_6_single_data}, {'name': 'method_7', 'data': method_7_single_data}, {'name': 'method_8', 'data': method_8_single_data}, {'name': 'method_9', 'data': method_9_single_data}, {'name': 'method_10', 'data': method_10_single_data}]
        # for each in series:
        #     if each['name'] == 'method_1':
        #         print(each)
        #         exit()
        return JsonResponse({
            'code': 200,
            'status': "SUCCESS",
            'result': {'categories': categories, 'series': series},
        })
    else:
        return JsonResponse({
            'code': 501,
            'status': "ERROR",
            'message': "There should be ajax method."
        })


def getLineChartData(request):
    if request.method == "POST":
        csv_data = models.CsvData.objects.filter(hour_slab__gte=request.POST['from_hour'], hour_slab__lte=request.POST['to_hour']).order_by('id')
        series = []
        # method_2_data = []
        # method_3_data = []
        for row_data in csv_data:
            series.append([row_data.calculated_miliseconds, float(row_data.method_1)])
            # method_2_data.append(float(row_data.method_2))
            # method_2_data.append("{:02d}".format(row_data.hour_slab) + ":" + row_data.calculated_time.strftime("%M") + ":" + row_data.calculated_time.strftime("%S"))
            # method_3_data.append(float(row_data.method_3))
            # method_3_data.append("{:02d}".format(row_data.hour_slab) + ":" + row_data.calculated_time.strftime("%M") + ":" + row_data.calculated_time.strftime("%S"))
        # series.append(
        #     {
        #         'name': 'method_1',
        #         'id': 'method_1',
        #         'marker': {
        #             'symbol': 'circle'
        #         },
        #         'data': method_1_data
        #     })
        # series.append(
        #     {
        #         'name': 'method_2',
        #         'id': 'method_2',
        #         'marker': {
        #             'symbol': 'circle'
        #         },
        #         'data': method_2_data
        #     })
        # series.append(
        #     {
        #         'name': 'method_3',
        #         'id': 'method_3',
        #         'marker': {
        #             'symbol': 'circle'
        #         },
        #         'data': method_3_data
        #     })
        return JsonResponse({
            'code': 200,
            'status': "SUCCESS",
            'result': {'series': series},
        })
    else:
        return JsonResponse({
            'code': 502,
            'status': "ERROR",
            'message': "There should be ajax method."
        })


def lineChart(request):
    total_hours = models.CsvData.objects.values('hour_slab').distinct()
    context.update({'total_hours': total_hours})
    return render(request, 'front/lineChart.html', context)
