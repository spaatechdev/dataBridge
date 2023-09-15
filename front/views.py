# from django.shortcuts import render, redirect
# from datetime import datetime
# from dataBridge import settings
# from django.contrib import messages
# from django.http import JsonResponse
# from django.core.files.storage import FileSystemStorage
# from . import models
# from django.db.models import Max, Min, Avg
# import os
# import math
# import csv
# import environ
# from collections import defaultdict
# import pymysql

# import environ
# env = environ.Env()
# environ.Env.read_env()

# context = {}
# context['project_name'] = env("PROJECT_NAME")
# context['client_name'] = env("CLIENT_NAME")

# # Create your views here.


# def millisToMinutesAndSeconds(millis=None):
#     minutes = math.floor(millis / 60000)
#     seconds = '{0:.2f}'.format((millis % 60000) / 1000)
#     return str(minutes) + ":" + str('0' if float(seconds) < 10 else '') + str(round(float(seconds)))


# def importCsv(request):
#     if request.method == "POST":
#         csv_list = []
#         if request.FILES.get('csv_data', None):
#             file = request.FILES['csv_data']
#             tmpname = str(datetime.now().microsecond) + \
#                 os.path.splitext(str(file))[1]
#             fs = FileSystemStorage(
#                 settings.MEDIA_ROOT + "csv/", settings.MEDIA_ROOT + "/csv/")
#             fs.save(tmpname, file)
#             file_name = "csv/" + tmpname

#             db = pymysql.connect(host=env("DATABASE_HOST"), user=env("DATABASE_USER"), password=env("DATABASE_PASSWORD"), db=env("DATABASE_NAME"))
#             with open(settings.MEDIA_ROOT + file_name, newline='', mode='r', encoding='ISO-8859-1') as csvfile:
#                 reader = csv.reader(csvfile)
#                 header = next(reader)
#             # Generate SQL to add new columns
#             alter_table_sql = f"ALTER TABLE test {', '.join(f'ADD COLUMN {col} VARCHAR(255)' for col in header)}"
#             # Execute dynamic SQL to add columns
#             cursor = db.cursor()
#             cursor.execute(alter_table_sql)

#             with open(settings.MEDIA_ROOT + file_name, newline='', mode='r', encoding='ISO-8859-1') as csvfile:
#                 next(csvfile)
#                 # reader = csv.DictReader(csvfile)
#                 reader = csv.reader(csvfile)
#                 # hour_slab = 0
#                 # flag = 0
#                 for row in reader:
#                     # if not row[0]:
#                     #     break
#                     # splitted = row[0].split(":")
#                     # totalMiliSeconds = int(splitted[0]) * 60000 + int(
#                     #     splitted[1].split(".")[0]) * 1000 + int(splitted[1].split(".")[1])
#                     # calculated_time = millisToMinutesAndSeconds(
#                     #     totalMiliSeconds)
#                     # if int(calculated_time.split(":")[0]) == 59:
#                     #     flag = 1
#                     #     # if len(csv_list) > 1000:
#                     #     #     models.CsvData.objects.bulk_create(csv_list)
#                     #     #     csv_list = []
#                     #     #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
#                     #     #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_time="00:"+calculated_time, hour_slab=hour_slab))
#                     #     # else:
#                     #     #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
#                     #     #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_time="00:"+calculated_time, hour_slab=hour_slab))

#                     # if flag == 1 and int(calculated_time.split(":")[0]) == 0:
#                     #     hour_slab += 1
#                     #     flag = 0
#                     #     # if len(csv_list) > 1000:
#                     #     #     models.CsvData.objects.bulk_create(csv_list)
#                     #     #     csv_list = []
#                     #     #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
#                     #     #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_time="00:"+calculated_time, hour_slab=hour_slab))
#                     #     # else:
#                     #     #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
#                     #     #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_time="00:"+calculated_time, hour_slab=hour_slab))

#                     # elif flag == 1 and int(calculated_time.split(":")[0]) != 0:
#                     #     hour_slab += 0
#                     #     # if len(csv_list) > 1000:
#                     #     #     models.CsvData.objects.bulk_create(csv_list)
#                     #     #     csv_list = []
#                     #     #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
#                     #     #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_time="00:"+calculated_time, hour_slab=hour_slab))
#                     #     # else:
#                     #     #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
#                     #     #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_time="00:"+calculated_time, hour_slab=hour_slab))

#                     # if len(csv_list) > 1000:
#                     #     models.CsvData.objects.bulk_create(csv_list)
#                     #     csv_list = []
#                     #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
#                     #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_miliseconds=(hour_slab * 60 * 60 * 1000) + totalMiliSeconds, calculated_time="00:"+calculated_time, hour_slab=hour_slab))
#                     # else:
#                     #     csv_list.append(models.CsvData(time=row[0], method_1=row[1], method_2=row[2], method_3=row[3], method_4=row[4], method_5=row[5], method_6=row[6],
#                     #                     method_7=row[7], method_8=row[8], method_9=row[9], method_10=row[10], calculated_miliseconds=(hour_slab * 60 * 60 * 1000) + totalMiliSeconds, calculated_time="00:"+calculated_time, hour_slab=hour_slab))
#                     insert_sql = f"INSERT INTO test ({', '.join(header)}) VALUES ({', '.join(['%s'] * len(header))})"
#                     cursor.execute(insert_sql, row)

#                 # models.CsvData.objects.bulk_create(csv_list)
#                 # csvfile.close()
#                 # os.remove(settings.MEDIA_ROOT + file_name)
            
#             db.commit()
#             db.close()
#             messages.success(request, 'Csv Data Uploaded Successfully.')
#             return redirect('index')
#     return render(request, 'front/index.html', context)


# def scatterChart(request):
#     total_hours = models.CsvData.objects.values('hour_slab').distinct()
#     context.update({'total_hours': total_hours})
#     return render(request, 'front/scatterChart.html', context)


# def getScatterChartData(request):
#     if request.method == "POST":
#         hour = request.POST['hour']
#         csv_data = models.CsvData.objects.filter(hour_slab=int(hour))
#         categories = [
#             field.name for field in csv_data.model._meta.fields if field.name.startswith('method_')]
#         method_1_single_data = []
#         method_2_single_data = []
#         method_3_single_data = []
#         method_4_single_data = []
#         method_5_single_data = []
#         method_6_single_data = []
#         method_7_single_data = []
#         method_8_single_data = []
#         method_9_single_data = []
#         method_10_single_data = []
#         for row_data in csv_data:
#             method_1_single_data.append([0, float(row_data.method_1)])
#             method_2_single_data.append([1, float(row_data.method_2)])
#             method_3_single_data.append([2, float(row_data.method_3)])
#             method_4_single_data.append([3, float(row_data.method_4)])
#             method_5_single_data.append([4, float(row_data.method_5)])
#             method_6_single_data.append([5, float(row_data.method_6)])
#             method_7_single_data.append([6, float(row_data.method_7)])
#             method_8_single_data.append([7, float(row_data.method_8)])
#             method_9_single_data.append([8, float(row_data.method_9)])
#             method_10_single_data.append([9, float(row_data.method_10)])
#         series = [{'name': 'method_1', 'data': method_1_single_data}, {'name': 'method_2', 'data': method_2_single_data}, {'name': 'method_3', 'data': method_3_single_data}, {'name': 'method_4', 'data': method_4_single_data}, {'name': 'method_5', 'data': method_5_single_data}, {
#             'name': 'method_6', 'data': method_6_single_data}, {'name': 'method_7', 'data': method_7_single_data}, {'name': 'method_8', 'data': method_8_single_data}, {'name': 'method_9', 'data': method_9_single_data}, {'name': 'method_10', 'data': method_10_single_data}]
#         # for each in series:
#         #     if each['name'] == 'method_1':
#         #         print(each)
#         #         exit()
#         return JsonResponse({
#             'code': 200,
#             'status': "SUCCESS",
#             'result': {'categories': categories, 'series': series},
#         })
#     else:
#         return JsonResponse({
#             'code': 501,
#             'status': "ERROR",
#             'message': "There should be ajax method."
#         })


# def lineChart(request):
#     total_hours = models.CsvData.objects.values('hour_slab').distinct()
#     context.update({'total_hours': total_hours})
#     return render(request, 'front/lineChart.html', context)


# def getLineChartData(request):
#     if request.method == "POST":
#         csv_data = models.CsvData.objects.filter(
#             hour_slab__gte=request.POST['from_hour'], hour_slab__lte=request.POST['to_hour']).order_by('id')
#         series = []
#         # method_2_data = []
#         # method_3_data = []
#         for row_data in csv_data:
#             if int(request.POST['method']) == 1:
#                 series.append([row_data.calculated_miliseconds,
#                               float(row_data.method_1)])
#             elif int(request.POST['method']) == 2:
#                 series.append([row_data.calculated_miliseconds,
#                               float(row_data.method_2)])
#             elif int(request.POST['method']) == 3:
#                 series.append([row_data.calculated_miliseconds,
#                               float(row_data.method_3)])
#             elif int(request.POST['method']) == 4:
#                 series.append([row_data.calculated_miliseconds,
#                               float(row_data.method_4)])
#             elif int(request.POST['method']) == 5:
#                 series.append([row_data.calculated_miliseconds,
#                               float(row_data.method_5)])
#             elif int(request.POST['method']) == 6:
#                 series.append([row_data.calculated_miliseconds,
#                               float(row_data.method_6)])
#             elif int(request.POST['method']) == 7:
#                 series.append([row_data.calculated_miliseconds,
#                               float(row_data.method_7)])
#             elif int(request.POST['method']) == 8:
#                 series.append([row_data.calculated_miliseconds,
#                               float(row_data.method_8)])
#             elif int(request.POST['method']) == 9:
#                 series.append([row_data.calculated_miliseconds,
#                               float(row_data.method_9)])
#             elif int(request.POST['method']) == 10:
#                 series.append([row_data.calculated_miliseconds,
#                               float(row_data.method_10)])
#             # method_2_data.append(float(row_data.method_2))
#             # method_2_data.append("{:02d}".format(row_data.hour_slab) + ":" + row_data.calculated_time.strftime("%M") + ":" + row_data.calculated_time.strftime("%S"))
#             # method_3_data.append(float(row_data.method_3))
#             # method_3_data.append("{:02d}".format(row_data.hour_slab) + ":" + row_data.calculated_time.strftime("%M") + ":" + row_data.calculated_time.strftime("%S"))
#         # series.append(
#         #     {
#         #         'name': 'method_1',
#         #         'id': 'method_1',
#         #         'marker': {
#         #             'symbol': 'circle'
#         #         },
#         #         'data': method_1_data
#         #     })
#         # series.append(
#         #     {
#         #         'name': 'method_2',
#         #         'id': 'method_2',
#         #         'marker': {
#         #             'symbol': 'circle'
#         #         },
#         #         'data': method_2_data
#         #     })
#         # series.append(
#         #     {
#         #         'name': 'method_3',
#         #         'id': 'method_3',
#         #         'marker': {
#         #             'symbol': 'circle'
#         #         },
#         #         'data': method_3_data
#         #     })
#         return JsonResponse({
#             'code': 200,
#             'status': "SUCCESS",
#             'result': {'series': series},
#         })
#     else:
#         return JsonResponse({
#             'code': 502,
#             'status': "ERROR",
#             'message': "There should be ajax method."
#         })
    

# def getColumnCounts():
#     column_counts = []
#     column_count = len(models.CsvData._meta.fields) - 5
#     for i in range(1, column_count + 1):
#         column_counts.append(i)
#     return column_counts


# def multipleLineChart(request):
#     total_hours = models.CsvData.objects.values('hour_slab').distinct().order_by('hour_slab')
#     min_hour = "{:02d}".format(total_hours[0]['hour_slab'])
#     max_hour = "{:02d}".format(total_hours[len(total_hours) - 1]['hour_slab'])
#     column_counts = getColumnCounts()
#     context.update({'total_hours': total_hours, 'min_hour': min_hour, 'max_hour': max_hour, 'column_counts': column_counts})
#     return render(request, 'front/multipleLineChart.html', context)


# def getMultipleLineChartData(request):
#     if request.method == "POST":
#         chart_type = request.POST['chart_type']
#         bar_chart_type = request.POST['bar_chart_type']
        
#         if chart_type == 'line':
#             from_time = request.POST['from_time']
#             to_time = request.POST['to_time']
#             from_miliseconds = int(from_time.split(':')[0]) * 3600 * 1000 + int(from_time.split(':')[1]) * 60 * 1000
#             to_miliseconds = int(to_time.split(':')[0]) * 3600 * 1000 + int(to_time.split(':')[1]) * 60 * 1000

#             if from_miliseconds > to_miliseconds:
#                 return JsonResponse({
#                     'code': 503,
#                     'status': "ERROR",
#                     'message': "From time should not exceeds To time "
#                 })

#             # csv_data = models.CsvData.objects.filter(
#             #     hour_slab__gte=request.POST['from_time'], hour_slab__lte=request.POST['to_time']).order_by('id')
#             csv_data = models.CsvData.objects.filter(calculated_miliseconds__gte=from_miliseconds, calculated_miliseconds__lte=to_miliseconds).order_by('id')
#             # categories = []
#             series = []
#             column_counts = getColumnCounts()
#             dynamic_vars = {}
#             for index, element in enumerate(column_counts, start=1):
#                 dynamic_vars[f"method_{index}"] = []
#             for row_data in csv_data:
#                 # categories.append(millisToMinutesAndSeconds(row_data.calculated_miliseconds))
#                 for method in dynamic_vars:
#                     dynamic_vars[method].append([row_data.calculated_miliseconds, float(getattr(row_data, method))])
#             if '1' in request.POST.getlist('method'):
#                 series.append({'name': 'Sensor 1', 'data': dynamic_vars['method_1']})
#             if '2' in request.POST.getlist('method'):
#                 series.append({'name': 'Sensor 2', 'data': dynamic_vars['method_2']})
#             if '3' in request.POST.getlist('method'):
#                 series.append({'name': 'Sensor 3', 'data': dynamic_vars['method_3']})
#             if '4' in request.POST.getlist('method'):
#                 series.append({'name': 'Sensor 4', 'data': dynamic_vars['method_4']})
#             if '5' in request.POST.getlist('method'):
#                 series.append({'name': 'Sensor 5', 'data': dynamic_vars['method_5']})
#             if '6' in request.POST.getlist('method'):
#                 series.append({'name': 'Sensor 6', 'data': dynamic_vars['method_6']})
#             if '7' in request.POST.getlist('method'):
#                 series.append({'name': 'Sensor 7', 'data': dynamic_vars['method_7']})
#             if '8' in request.POST.getlist('method'):
#                 series.append({'name': 'Sensor 8', 'data': dynamic_vars['method_8']})
#             if '9' in request.POST.getlist('method'):
#                 series.append({'name': 'Sensor 9', 'data': dynamic_vars['method_9']})
#             if '10' in request.POST.getlist('method'):
#                 series.append({'name': 'Sensor 10', 'data': dynamic_vars['method_10']})
#             return JsonResponse({
#                 'code': 200,
#                 'status': "SUCCESS",
#                 'result': {'series': series, 'chart_type': chart_type},
#             })
#         elif chart_type == 'bar':
#             from_time = request.POST['bar_from_time']
#             to_time = request.POST['bar_to_time']
#             from_miliseconds = int(from_time) * 3600 * 1000
#             to_miliseconds = int(to_time) * 3600 * 1000
#             # from_miliseconds = int(from_time.split(':')[0]) * 3600 * 1000 + int(from_time.split(':')[1]) * 60 * 1000
#             # to_miliseconds = (int(to_time.split(':')[0]) + 1) * 3600 * 1000 + int(to_time.split(':')[1]) * 60 * 1000
#             if from_miliseconds > to_miliseconds:
#                 return JsonResponse({
#                     'code': 504,
#                     'status': "ERROR",
#                     'message': "From time should not exceeds To time "
#                 })
#             if bar_chart_type == 'max':
#                 # csv_data = models.CsvData.objects.filter(calculated_miliseconds__gte=from_miliseconds, calculated_miliseconds__lte=to_miliseconds).values('hour_slab').annotate(val_method_1=Max('method_1'), val_method_2=Max('method_2'), val_method_3=Max('method_3'), val_method_4=Max('method_4'), val_method_5=Max('method_5'), val_method_6=Max('method_6'), val_method_7=Max('method_7'), val_method_8=Max('method_8'), val_method_9=Max('method_9'), val_method_10=Max('method_10')).order_by('id')
#                 csv_data = models.CsvData.objects.values('hour_slab').filter(calculated_miliseconds__gte=from_miliseconds, calculated_miliseconds__lte=to_miliseconds).annotate(
#                     val_method_1=Max('method_1'),
#                     val_method_2=Max('method_2'),
#                     val_method_3=Max('method_3'),
#                     val_method_4=Max('method_4'),
#                     val_method_5=Max('method_5'),
#                     val_method_6=Max('method_6'),
#                     val_method_7=Max('method_7'),
#                     val_method_8=Max('method_8'),
#                     val_method_9=Max('method_9'),
#                     val_method_10=Max('method_10')
#                 )
#                 aggregated_data = defaultdict(float)
#                 for item in csv_data:
#                     aggregated_data[item['hour_slab']] = [item['val_method_1'], item['val_method_2'], item['val_method_3'], item['val_method_4'], item['val_method_5'], item['val_method_6'], item['val_method_7'], item['val_method_8'], item['val_method_9'], item['val_method_10']]
#                 categories = []
#                 series = []

#                 column_counts = getColumnCounts()
#                 dynamic_vars = {}
#                 for index, element in enumerate(column_counts, start=1):
#                     dynamic_vars[f"Sensor {index}"] = {}
#                 for method in dynamic_vars:
#                     dynamic_vars[method]['name'] = method
#                     dynamic_vars[method]['data'] = []
#                 for hour_slab, average_data in aggregated_data.items():
#                     if int(from_time) <= hour_slab or int(to_time) >= hour_slab:
#                         categories.append("Hour " + str(hour_slab))
#                         dynamic_vars["Sensor 1"]["data"].append(float(round(average_data[0], 2)))
#                         dynamic_vars["Sensor 2"]["data"].append(float(round(average_data[1], 2)))
#                         dynamic_vars["Sensor 3"]["data"].append(float(round(average_data[2], 2)))
#                         dynamic_vars["Sensor 4"]["data"].append(float(round(average_data[3], 2)))
#                         dynamic_vars["Sensor 5"]["data"].append(float(round(average_data[4], 2)))
#                         dynamic_vars["Sensor 6"]["data"].append(float(round(average_data[5], 2)))
#                         dynamic_vars["Sensor 7"]["data"].append(float(round(average_data[6], 2)))
#                         dynamic_vars["Sensor 8"]["data"].append(float(round(average_data[7], 2)))
#                         dynamic_vars["Sensor 9"]["data"].append(float(round(average_data[8], 2)))
#                         dynamic_vars["Sensor 10"]["data"].append(float(round(average_data[9], 2)))
#                 if '1' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 1'])
#                 if '2' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 2'])
#                 if '3' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 3'])
#                 if '4' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 4'])
#                 if '5' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 5'])
#                 if '6' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 6'])
#                 if '7' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 7'])
#                 if '8' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 8'])
#                 if '9' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 9'])
#                 if '10' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 10'])
#             if bar_chart_type == 'min':
#                 csv_data = models.CsvData.objects.values('hour_slab').filter(calculated_miliseconds__gte=from_miliseconds, calculated_miliseconds__lte=to_miliseconds).annotate(
#                     val_method_1=Min('method_1'),
#                     val_method_2=Min('method_2'),
#                     val_method_3=Min('method_3'),
#                     val_method_4=Min('method_4'),
#                     val_method_5=Min('method_5'),
#                     val_method_6=Min('method_6'),
#                     val_method_7=Min('method_7'),
#                     val_method_8=Min('method_8'),
#                     val_method_9=Min('method_9'),
#                     val_method_10=Min('method_10')
#                 )
#                 aggregated_data = defaultdict(float)

#                 for item in csv_data:
#                     aggregated_data[item['hour_slab']] = [item['val_method_1'], item['val_method_2'], item['val_method_3'], item['val_method_4'], item['val_method_5'], item['val_method_6'], item['val_method_7'], item['val_method_8'], item['val_method_9'], item['val_method_10']]
#                 categories = []
#                 series = []

#                 column_counts = getColumnCounts()
#                 dynamic_vars = {}
#                 for index, element in enumerate(column_counts, start=1):
#                     dynamic_vars[f"Sensor {index}"] = {}
#                 for method in dynamic_vars:
#                     dynamic_vars[method]['name'] = method
#                     dynamic_vars[method]['data'] = []
#                 for hour_slab, average_data in aggregated_data.items():
#                     if int(from_time) <= hour_slab or int(to_time) >= hour_slab:
#                         categories.append("Hour " + str(hour_slab))
#                         dynamic_vars["Sensor 1"]["data"].append(float(round(average_data[0], 2)))
#                         dynamic_vars["Sensor 2"]["data"].append(float(round(average_data[1], 2)))
#                         dynamic_vars["Sensor 3"]["data"].append(float(round(average_data[2], 2)))
#                         dynamic_vars["Sensor 4"]["data"].append(float(round(average_data[3], 2)))
#                         dynamic_vars["Sensor 5"]["data"].append(float(round(average_data[4], 2)))
#                         dynamic_vars["Sensor 6"]["data"].append(float(round(average_data[5], 2)))
#                         dynamic_vars["Sensor 7"]["data"].append(float(round(average_data[6], 2)))
#                         dynamic_vars["Sensor 8"]["data"].append(float(round(average_data[7], 2)))
#                         dynamic_vars["Sensor 9"]["data"].append(float(round(average_data[8], 2)))
#                         dynamic_vars["Sensor 10"]["data"].append(float(round(average_data[9], 2)))
#                 if '1' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 1'])
#                 if '2' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 2'])
#                 if '3' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 3'])
#                 if '4' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 4'])
#                 if '5' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 5'])
#                 if '6' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 6'])
#                 if '7' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 7'])
#                 if '8' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 8'])
#                 if '9' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 9'])
#                 if '10' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 10'])
#             if bar_chart_type == 'avg':
#                 csv_data = models.CsvData.objects.values('hour_slab').filter(calculated_miliseconds__gte=from_miliseconds, calculated_miliseconds__lte=to_miliseconds).annotate(
#                     val_method_1=Avg('method_1'),
#                     val_method_2=Avg('method_2'),
#                     val_method_3=Avg('method_3'),
#                     val_method_4=Avg('method_4'),
#                     val_method_5=Avg('method_5'),
#                     val_method_6=Avg('method_6'),
#                     val_method_7=Avg('method_7'),
#                     val_method_8=Avg('method_8'),
#                     val_method_9=Avg('method_9'),
#                     val_method_10=Avg('method_10')
#                 )
#                 aggregated_data = defaultdict(float)

#                 for item in csv_data:
#                     aggregated_data[item['hour_slab']] = [item['val_method_1'], item['val_method_2'], item['val_method_3'], item['val_method_4'], item['val_method_5'], item['val_method_6'], item['val_method_7'], item['val_method_8'], item['val_method_9'], item['val_method_10']]
#                 categories = []
#                 series = []

#                 column_counts = getColumnCounts()
#                 dynamic_vars = {}
#                 for index, element in enumerate(column_counts, start=1):
#                     dynamic_vars[f"Sensor {index}"] = {}
#                 for method in dynamic_vars:
#                     dynamic_vars[method]['name'] = method
#                     dynamic_vars[method]['data'] = []
#                 for hour_slab, average_data in aggregated_data.items():
#                     if int(from_time) <= hour_slab or int(to_time) >= hour_slab:
#                         categories.append("Hour " + str(hour_slab))
#                         dynamic_vars["Sensor 1"]["data"].append(float(round(average_data[0], 2)))
#                         dynamic_vars["Sensor 2"]["data"].append(float(round(average_data[1], 2)))
#                         dynamic_vars["Sensor 3"]["data"].append(float(round(average_data[2], 2)))
#                         dynamic_vars["Sensor 4"]["data"].append(float(round(average_data[3], 2)))
#                         dynamic_vars["Sensor 5"]["data"].append(float(round(average_data[4], 2)))
#                         dynamic_vars["Sensor 6"]["data"].append(float(round(average_data[5], 2)))
#                         dynamic_vars["Sensor 7"]["data"].append(float(round(average_data[6], 2)))
#                         dynamic_vars["Sensor 8"]["data"].append(float(round(average_data[7], 2)))
#                         dynamic_vars["Sensor 9"]["data"].append(float(round(average_data[8], 2)))
#                         dynamic_vars["Sensor 10"]["data"].append(float(round(average_data[9], 2)))
#                 if '1' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 1'])
#                 if '2' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 2'])
#                 if '3' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 3'])
#                 if '4' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 4'])
#                 if '5' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 5'])
#                 if '6' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 6'])
#                 if '7' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 7'])
#                 if '8' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 8'])
#                 if '9' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 9'])
#                 if '10' in request.POST.getlist('method'):
#                     series.append(dynamic_vars['Sensor 10'])
#             return JsonResponse({
#                 'code': 200,
#                 'status': "SUCCESS",
#                 'result': {'series': series, 'categories': categories, 'chart_type': chart_type},
#             })
#     else:
#         return JsonResponse({
#             'code': 502,
#             'status': "ERROR",
#             'message': "There should be ajax method."
#         })




from django.shortcuts import render, redirect
from datetime import datetime
from dataBridge import settings
from django.contrib import messages
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from . import models
from django.db.models import Max, Min, Avg
import os
import math
import csv
import environ
from collections import defaultdict

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
                next(csvfile)
                # reader = csv.DictReader(csvfile)
                reader = csv.reader(csvfile)
                hour_slab = 0
                flag = 0
                for row in reader:
                    if not row[0]:
                        break
                    splitted = row[0].split(":")
                    totalMiliSeconds = int(splitted[0]) * 60000 + int(
                        splitted[1].split(".")[0]) * 1000 + int(splitted[1].split(".")[1])
                    calculated_time = millisToMinutesAndSeconds(
                        totalMiliSeconds)
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


def lineChart(request):
    total_hours = models.CsvData.objects.values('hour_slab').distinct()
    context.update({'total_hours': total_hours})
    return render(request, 'front/lineChart.html', context)


def getLineChartData(request):
    if request.method == "POST":
        csv_data = models.CsvData.objects.filter(
            hour_slab__gte=request.POST['from_hour'], hour_slab__lte=request.POST['to_hour']).order_by('id')
        series = []
        # method_2_data = []
        # method_3_data = []
        for row_data in csv_data:
            if int(request.POST['method']) == 1:
                series.append([row_data.calculated_miliseconds,
                              float(row_data.method_1)])
            elif int(request.POST['method']) == 2:
                series.append([row_data.calculated_miliseconds,
                              float(row_data.method_2)])
            elif int(request.POST['method']) == 3:
                series.append([row_data.calculated_miliseconds,
                              float(row_data.method_3)])
            elif int(request.POST['method']) == 4:
                series.append([row_data.calculated_miliseconds,
                              float(row_data.method_4)])
            elif int(request.POST['method']) == 5:
                series.append([row_data.calculated_miliseconds,
                              float(row_data.method_5)])
            elif int(request.POST['method']) == 6:
                series.append([row_data.calculated_miliseconds,
                              float(row_data.method_6)])
            elif int(request.POST['method']) == 7:
                series.append([row_data.calculated_miliseconds,
                              float(row_data.method_7)])
            elif int(request.POST['method']) == 8:
                series.append([row_data.calculated_miliseconds,
                              float(row_data.method_8)])
            elif int(request.POST['method']) == 9:
                series.append([row_data.calculated_miliseconds,
                              float(row_data.method_9)])
            elif int(request.POST['method']) == 10:
                series.append([row_data.calculated_miliseconds,
                              float(row_data.method_10)])
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
    

def getColumnCounts():
    column_count = len(models.CsvData._meta.fields) - 5
    first_row = models.CsvData.objects.get(pk=1)
    column_counts = []
    if first_row.method_1 == "":
        column_count -= 1
    elif first_row.method_2 == "":
        column_count -= 1
    elif first_row.method_3 == "":
        column_count -= 1
    elif first_row.method_4 == "":
        column_count -= 1
    elif first_row.method_5 == "":
        column_count -= 1
    elif first_row.method_6 == "":
        column_count -= 1
    elif first_row.method_7 == "":
        column_count -= 1
    elif first_row.method_8 == "":
        column_count -= 1
    elif first_row.method_9 == "":
        column_count -= 1
    elif first_row.method_10 == "":
        column_count -= 1
    for i in range(1, 11):
        column_counts.append(i)
    return column_counts


def multipleLineChart(request):
    total_hours = models.CsvData.objects.values('hour_slab').distinct().order_by('hour_slab')
    min_hour = "{:02d}".format(total_hours[0]['hour_slab'])
    max_hour = "{:02d}".format(total_hours[len(total_hours) - 1]['hour_slab'])
    column_counts = getColumnCounts()
    context.update({'total_hours': total_hours, 'min_hour': min_hour, 'max_hour': max_hour, 'column_counts': column_counts})
    return render(request, 'front/multipleLineChart.html', context)


def getMultipleLineChartData(request):
    if request.method == "POST":
        chart_type = request.POST['chart_type']
        bar_chart_type = request.POST['bar_chart_type']
        
        if chart_type == 'line':
            from_time = request.POST['from_time']
            to_time = request.POST['to_time']
            from_miliseconds = int(from_time.split(':')[0]) * 3600 * 1000 + int(from_time.split(':')[1]) * 60 * 1000
            to_miliseconds = int(to_time.split(':')[0]) * 3600 * 1000 + int(to_time.split(':')[1]) * 60 * 1000

            if from_miliseconds > to_miliseconds:
                return JsonResponse({
                    'code': 503,
                    'status': "ERROR",
                    'message': "From time should not exceeds To time "
                })

            # csv_data = models.CsvData.objects.filter(
            #     hour_slab__gte=request.POST['from_time'], hour_slab__lte=request.POST['to_time']).order_by('id')
            csv_data = models.CsvData.objects.filter(calculated_miliseconds__gte=from_miliseconds, calculated_miliseconds__lte=to_miliseconds).order_by('id')
            # categories = []
            series = []
            column_counts = getColumnCounts()
            dynamic_vars = {}
            for index, element in enumerate(column_counts, start=1):
                dynamic_vars[f"method_{index}"] = []
            for row_data in csv_data:
                # categories.append(millisToMinutesAndSeconds(row_data.calculated_miliseconds))
                for method in dynamic_vars:
                    dynamic_vars[method].append([row_data.calculated_miliseconds, float(getattr(row_data, method))])
            if '1' in request.POST.getlist('method'):
                series.append({'name': 'Sensor 1', 'data': dynamic_vars['method_1']})
            if '2' in request.POST.getlist('method'):
                series.append({'name': 'Sensor 2', 'data': dynamic_vars['method_2']})
            if '3' in request.POST.getlist('method'):
                series.append({'name': 'Sensor 3', 'data': dynamic_vars['method_3']})
            if '4' in request.POST.getlist('method'):
                series.append({'name': 'Sensor 4', 'data': dynamic_vars['method_4']})
            if '5' in request.POST.getlist('method'):
                series.append({'name': 'Sensor 5', 'data': dynamic_vars['method_5']})
            if '6' in request.POST.getlist('method'):
                series.append({'name': 'Sensor 6', 'data': dynamic_vars['method_6']})
            if '7' in request.POST.getlist('method'):
                series.append({'name': 'Sensor 7', 'data': dynamic_vars['method_7']})
            if '8' in request.POST.getlist('method'):
                series.append({'name': 'Sensor 8', 'data': dynamic_vars['method_8']})
            if '9' in request.POST.getlist('method'):
                series.append({'name': 'Sensor 9', 'data': dynamic_vars['method_9']})
            if '10' in request.POST.getlist('method'):
                series.append({'name': 'Sensor 10', 'data': dynamic_vars['method_10']})
            return JsonResponse({
                'code': 200,
                'status': "SUCCESS",
                'result': {'series': series, 'chart_type': chart_type},
            })
        elif chart_type == 'bar':
            from_time = request.POST['bar_from_time']
            to_time = request.POST['bar_to_time']
            from_miliseconds = int(from_time) * 3600 * 1000
            to_miliseconds = int(to_time) * 3600 * 1000
            # from_miliseconds = int(from_time.split(':')[0]) * 3600 * 1000 + int(from_time.split(':')[1]) * 60 * 1000
            # to_miliseconds = (int(to_time.split(':')[0]) + 1) * 3600 * 1000 + int(to_time.split(':')[1]) * 60 * 1000
            if from_miliseconds > to_miliseconds:
                return JsonResponse({
                    'code': 504,
                    'status': "ERROR",
                    'message': "From time should not exceeds To time "
                })
            if bar_chart_type == 'max':
                # csv_data = models.CsvData.objects.filter(calculated_miliseconds__gte=from_miliseconds, calculated_miliseconds__lte=to_miliseconds).values('hour_slab').annotate(val_method_1=Max('method_1'), val_method_2=Max('method_2'), val_method_3=Max('method_3'), val_method_4=Max('method_4'), val_method_5=Max('method_5'), val_method_6=Max('method_6'), val_method_7=Max('method_7'), val_method_8=Max('method_8'), val_method_9=Max('method_9'), val_method_10=Max('method_10')).order_by('id')
                csv_data = models.CsvData.objects.values('hour_slab').filter(calculated_miliseconds__gte=from_miliseconds, calculated_miliseconds__lte=to_miliseconds).annotate(
                    val_method_1=Max('method_1'),
                    val_method_2=Max('method_2'),
                    val_method_3=Max('method_3'),
                    val_method_4=Max('method_4'),
                    val_method_5=Max('method_5'),
                    val_method_6=Max('method_6'),
                    val_method_7=Max('method_7'),
                    val_method_8=Max('method_8'),
                    val_method_9=Max('method_9'),
                    val_method_10=Max('method_10')
                )
                aggregated_data = defaultdict(float)
                for item in csv_data:
                    aggregated_data[item['hour_slab']] = [item['val_method_1'], item['val_method_2'], item['val_method_3'], item['val_method_4'], item['val_method_5'], item['val_method_6'], item['val_method_7'], item['val_method_8'], item['val_method_9'], item['val_method_10']]
                categories = []
                series = []

                column_counts = getColumnCounts()
                dynamic_vars = {}
                for index, element in enumerate(column_counts, start=1):
                    dynamic_vars[f"Sensor {index}"] = {}
                for method in dynamic_vars:
                    dynamic_vars[method]['name'] = method
                    dynamic_vars[method]['data'] = []
                for hour_slab, average_data in aggregated_data.items():
                    if int(from_time) <= hour_slab or int(to_time) >= hour_slab:
                        categories.append("Hour " + str(hour_slab))
                        dynamic_vars["Sensor 1"]["data"].append(float(round(average_data[0], 2)))
                        dynamic_vars["Sensor 2"]["data"].append(float(round(average_data[1], 2)))
                        dynamic_vars["Sensor 3"]["data"].append(float(round(average_data[2], 2)))
                        dynamic_vars["Sensor 4"]["data"].append(float(round(average_data[3], 2)))
                        dynamic_vars["Sensor 5"]["data"].append(float(round(average_data[4], 2)))
                        dynamic_vars["Sensor 6"]["data"].append(float(round(average_data[5], 2)))
                        dynamic_vars["Sensor 7"]["data"].append(float(round(average_data[6], 2)))
                        dynamic_vars["Sensor 8"]["data"].append(float(round(average_data[7], 2)))
                        dynamic_vars["Sensor 9"]["data"].append(float(round(average_data[8], 2)))
                        dynamic_vars["Sensor 10"]["data"].append(float(round(average_data[9], 2)))
                if '1' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 1'])
                if '2' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 2'])
                if '3' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 3'])
                if '4' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 4'])
                if '5' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 5'])
                if '6' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 6'])
                if '7' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 7'])
                if '8' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 8'])
                if '9' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 9'])
                if '10' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 10'])
            if bar_chart_type == 'min':
                csv_data = models.CsvData.objects.values('hour_slab').filter(calculated_miliseconds__gte=from_miliseconds, calculated_miliseconds__lte=to_miliseconds).annotate(
                    val_method_1=Min('method_1'),
                    val_method_2=Min('method_2'),
                    val_method_3=Min('method_3'),
                    val_method_4=Min('method_4'),
                    val_method_5=Min('method_5'),
                    val_method_6=Min('method_6'),
                    val_method_7=Min('method_7'),
                    val_method_8=Min('method_8'),
                    val_method_9=Min('method_9'),
                    val_method_10=Min('method_10')
                )
                aggregated_data = defaultdict(float)

                for item in csv_data:
                    aggregated_data[item['hour_slab']] = [item['val_method_1'], item['val_method_2'], item['val_method_3'], item['val_method_4'], item['val_method_5'], item['val_method_6'], item['val_method_7'], item['val_method_8'], item['val_method_9'], item['val_method_10']]
                categories = []
                series = []

                column_counts = getColumnCounts()
                dynamic_vars = {}
                for index, element in enumerate(column_counts, start=1):
                    dynamic_vars[f"Sensor {index}"] = {}
                for method in dynamic_vars:
                    dynamic_vars[method]['name'] = method
                    dynamic_vars[method]['data'] = []
                for hour_slab, average_data in aggregated_data.items():
                    if int(from_time) <= hour_slab or int(to_time) >= hour_slab:
                        categories.append("Hour " + str(hour_slab))
                        dynamic_vars["Sensor 1"]["data"].append(float(round(average_data[0], 2)))
                        dynamic_vars["Sensor 2"]["data"].append(float(round(average_data[1], 2)))
                        dynamic_vars["Sensor 3"]["data"].append(float(round(average_data[2], 2)))
                        dynamic_vars["Sensor 4"]["data"].append(float(round(average_data[3], 2)))
                        dynamic_vars["Sensor 5"]["data"].append(float(round(average_data[4], 2)))
                        dynamic_vars["Sensor 6"]["data"].append(float(round(average_data[5], 2)))
                        dynamic_vars["Sensor 7"]["data"].append(float(round(average_data[6], 2)))
                        dynamic_vars["Sensor 8"]["data"].append(float(round(average_data[7], 2)))
                        dynamic_vars["Sensor 9"]["data"].append(float(round(average_data[8], 2)))
                        dynamic_vars["Sensor 10"]["data"].append(float(round(average_data[9], 2)))
                if '1' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 1'])
                if '2' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 2'])
                if '3' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 3'])
                if '4' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 4'])
                if '5' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 5'])
                if '6' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 6'])
                if '7' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 7'])
                if '8' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 8'])
                if '9' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 9'])
                if '10' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 10'])
            if bar_chart_type == 'avg':
                csv_data = models.CsvData.objects.values('hour_slab').filter(calculated_miliseconds__gte=from_miliseconds, calculated_miliseconds__lte=to_miliseconds).annotate(
                    val_method_1=Avg('method_1'),
                    val_method_2=Avg('method_2'),
                    val_method_3=Avg('method_3'),
                    val_method_4=Avg('method_4'),
                    val_method_5=Avg('method_5'),
                    val_method_6=Avg('method_6'),
                    val_method_7=Avg('method_7'),
                    val_method_8=Avg('method_8'),
                    val_method_9=Avg('method_9'),
                    val_method_10=Avg('method_10')
                )
                aggregated_data = defaultdict(float)

                for item in csv_data:
                    aggregated_data[item['hour_slab']] = [item['val_method_1'], item['val_method_2'], item['val_method_3'], item['val_method_4'], item['val_method_5'], item['val_method_6'], item['val_method_7'], item['val_method_8'], item['val_method_9'], item['val_method_10']]
                categories = []
                series = []

                column_counts = getColumnCounts()
                dynamic_vars = {}
                for index, element in enumerate(column_counts, start=1):
                    dynamic_vars[f"Sensor {index}"] = {}
                for method in dynamic_vars:
                    dynamic_vars[method]['name'] = method
                    dynamic_vars[method]['data'] = []
                for hour_slab, average_data in aggregated_data.items():
                    if int(from_time) <= hour_slab or int(to_time) >= hour_slab:
                        categories.append("Hour " + str(hour_slab))
                        dynamic_vars["Sensor 1"]["data"].append(float(round(average_data[0], 2)))
                        dynamic_vars["Sensor 2"]["data"].append(float(round(average_data[1], 2)))
                        dynamic_vars["Sensor 3"]["data"].append(float(round(average_data[2], 2)))
                        dynamic_vars["Sensor 4"]["data"].append(float(round(average_data[3], 2)))
                        dynamic_vars["Sensor 5"]["data"].append(float(round(average_data[4], 2)))
                        dynamic_vars["Sensor 6"]["data"].append(float(round(average_data[5], 2)))
                        dynamic_vars["Sensor 7"]["data"].append(float(round(average_data[6], 2)))
                        dynamic_vars["Sensor 8"]["data"].append(float(round(average_data[7], 2)))
                        dynamic_vars["Sensor 9"]["data"].append(float(round(average_data[8], 2)))
                        dynamic_vars["Sensor 10"]["data"].append(float(round(average_data[9], 2)))
                if '1' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 1'])
                if '2' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 2'])
                if '3' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 3'])
                if '4' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 4'])
                if '5' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 5'])
                if '6' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 6'])
                if '7' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 7'])
                if '8' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 8'])
                if '9' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 9'])
                if '10' in request.POST.getlist('method'):
                    series.append(dynamic_vars['Sensor 10'])
            return JsonResponse({
                'code': 200,
                'status': "SUCCESS",
                'result': {'series': series, 'categories': categories, 'chart_type': chart_type},
            })
    else:
        return JsonResponse({
            'code': 502,
            'status': "ERROR",
            'message': "There should be ajax method."
        })