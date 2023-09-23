from django.shortcuts import render, redirect
from datetime import datetime
from decimal import Decimal
from dataBridge import settings
from django.contrib import messages
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from . import models
from . import constants
from django.db.models import Max, Min, Avg
import os
import math
import pathlib
import csv
import environ
import json
import openpyxl
from django.db import connections
from django.contrib.messages import get_messages
import re
from collections import defaultdict

import environ
env = environ.Env()
environ.Env.read_env()

context = {}
context['project_name'] = env("PROJECT_NAME")
context['client_name'] = env("CLIENT_NAME")

# Create your views here.
def get_constants(sensor_type):
    if sensor_type == 'strain':
        file_path = "templates/constants/strain_columns.txt"
        f = open(file_path)
        columns = f.read()
        if columns == "":
            columns = json.dumps(constants.strain_columns)
            f = open(file_path, "w+")
            f.write(columns)
        f.close()
        return json.loads(columns)
    if sensor_type == 'tilt':
        file_path = "templates/constants/tilt_columns.txt"
        f = open(file_path)
        columns = f.read()
        if columns == "":
            columns = json.dumps(constants.tilt_columns)
            f = open(file_path, "w+")
            f.write(columns)
        f.close()
        return json.loads(columns)
    if sensor_type == 'displacement':
        file_path = "templates/constants/displacement_columns.txt"
        f = open(file_path)
        columns = f.read()
        if columns == "":
            columns = json.dumps(constants.displacement_columns)
            f = open(file_path, "w+")
            f.write(columns)
        f.close()
        return json.loads(columns)
    if sensor_type == 'settlement':
        file_path = "templates/constants/settlement_columns.txt"
        f = open(file_path)
        columns = f.read()
        if columns == "":
            columns = json.dumps(constants.settlement_columns)
            f = open(file_path, "w+")
            f.write(columns)
        f.close()
        return json.loads(columns)
    if sensor_type == 'vibration':
        file_path = "templates/constants/vibration_columns.txt"
        f = open(file_path)
        columns = f.read()
        if columns == "":
            columns = json.dumps(constants.vibration_columns)
            f = open(file_path, "w+")
            f.write(columns)
        f.close()
        return json.loads(columns)
    

def getSensorsByTypes(request):
    if request.method == "POST":
        sensor_type = request.POST['sensor_type']
        sensor_names = get_constants(sensor_type)
        columns = {k: v for k, v in sensor_names.items() if not v.startswith('test_method_')}

        if sensor_type == 'strain':
            min_time = (models.StrainData.objects.all().order_by('date_time')[0].date_time).strftime("%Y-%m-%dT%H:%M:%S")
            max_time = (models.StrainData.objects.all().order_by('-date_time')[0].date_time).strftime("%Y-%m-%dT%H:%M:%S")
        if sensor_type == 'tilt':
            min_time = (models.TiltData.objects.all().order_by('date_time')[0].date_time).strftime("%Y-%m-%dT%H:%M:%S")
            max_time = (models.TiltData.objects.all().order_by('-date_time')[0].date_time).strftime("%Y-%m-%dT%H:%M:%S")
        if sensor_type == 'displacement':
            min_time = (models.DisplacementData.objects.all().order_by('date_time')[0].date_time).strftime("%Y-%m-%dT%H:%M:%S")
            max_time = (models.DisplacementData.objects.all().order_by('-date_time')[0].date_time).strftime("%Y-%m-%dT%H:%M:%S")
        if sensor_type == 'settlement':
            min_time = (models.SettlementData.objects.all().order_by('date_time')[0].date_time).strftime("%Y-%m-%dT%H:%M:%S")
            max_time = (models.SettlementData.objects.all().order_by('-date_time')[0].date_time).strftime("%Y-%m-%dT%H:%M:%S")
        if sensor_type == 'vibration':
            min_time = (models.VibrationData.objects.all().order_by('date_time')[0].date_time).strftime("%Y-%m-%dT%H:%M:%S")
            max_time = (models.VibrationData.objects.all().order_by('-date_time')[0].date_time).strftime("%Y-%m-%dT%H:%M:%S")
        return JsonResponse({
            'code': 200,
            'status': "SUCCESS",
            'columns': columns,
            'min_time': min_time,
            'max_time': max_time
        })
    else:
        return JsonResponse({
            'code': 501,
            'status': "ERROR",
            'message': "There should be ajax method"
        })


def getSensorCounts(sensor_type):
    if sensor_type == 'strain':
        column_names = []
        file_path = "templates/constants/strain_columns.txt"
        f = open(file_path)
        columns_constants = f.read()
        f.close()
        columns_constants = json.loads(columns_constants)

        columns_fields = [field.name for field in models.StrainData._meta.get_fields()]
        for each in columns_fields:
            if each.startswith('test_method_') and columns_constants[each] != each:
                column_names.append(columns_constants[each])
        return column_names
    if sensor_type == 'tilt':
        column_names = []
        file_path = "templates/constants/tilt_columns.txt"
        f = open(file_path)
        columns_constants = f.read()
        f.close()
        columns_constants = json.loads(columns_constants)

        columns_fields = [field.name for field in models.TiltData._meta.get_fields()]
        for each in columns_fields:
            if each.startswith('test_method_') and columns_constants[each] != each:
                column_names.append(columns_constants[each])
        return column_names
    if sensor_type == 'displacement':
        column_names = []
        file_path = "templates/constants/displacement_columns.txt"
        f = open(file_path)
        columns_constants = f.read()
        f.close()
        columns_constants = json.loads(columns_constants)

        columns_fields = [field.name for field in models.DisplacementData._meta.get_fields()]
        for each in columns_fields:
            if each.startswith('test_method_') and columns_constants[each] != each:
                column_names.append(columns_constants[each])
        return column_names
    if sensor_type == 'settlement':
        column_names = []
        file_path = "templates/constants/settlement_columns.txt"
        f = open(file_path)
        columns_constants = f.read()
        f.close()
        columns_constants = json.loads(columns_constants)

        columns_fields = [field.name for field in models.SettlementData._meta.get_fields()]
        for each in columns_fields:
            if each.startswith('test_method_') and columns_constants[each] != each:
                column_names.append(columns_constants[each])
        return column_names
    if sensor_type == 'vibration':
        column_names = []
        file_path = "templates/constants/vibration_columns.txt"
        f = open(file_path)
        columns_constants = f.read()
        f.close()
        columns_constants = json.loads(columns_constants)

        columns_fields = [field.name for field in models.VibrationData._meta.get_fields()]
        for each in columns_fields:
            if each.startswith('test_method_') and columns_constants[each] != each:
                column_names.append(columns_constants[each])
        return column_names


def index(request):
    strain_data = models.StrainData.objects.count()
    if strain_data == 0:
        # Delete all messages by popping them from the list
        try:
            storage = get_messages(request)
            for message in storage:
                message = ''
            storage.used = False
        except:
            pass
        messages.error(request, 'No Strain Data Is Present.')
        return redirect('importCsv')
    tilt_data = models.TiltData.objects.count()
    if tilt_data == 0:
        # Delete all messages by popping them from the list
        try:
            storage = get_messages(request)
            for message in storage:
                message = ''
            storage.used = False
        except:
            pass
        messages.error(request, 'No Tilt Data Is Present.')
        return redirect('importCsv')
    displacement_data = models.DisplacementData.objects.count()
    if displacement_data == 0:
        # Delete all messages by popping them from the list
        try:
            storage = get_messages(request)
            for message in storage:
                message = ''
            storage.used = False
        except:
            pass
        messages.error(request, 'No Displacement Data Is Present.')
        return redirect('importCsv')
    settlement_data = models.SettlementData.objects.count()
    if settlement_data == 0:
        # Delete all messages by popping them from the list
        try:
            storage = get_messages(request)
            for message in storage:
                message = ''
            storage.used = False
        except:
            pass
        messages.error(request, 'No Settlement Data Is Present.')
        return redirect('importCsv')
    vibration_data = models.VibrationData.objects.count()
    if vibration_data == 0:
        # Delete all messages by popping them from the list
        try:
            storage = get_messages(request)
            for message in storage:
                message = ''
            storage.used = False
        except:
            pass
        messages.error(request, 'No Vibration Data Is Present.')
        return redirect('importCsv')
    # strain_sensor_counts = getSensorCounts('strain')
    # tilt_sensor_counts = getSensorCounts('tilt')
    # displacement_sensor_counts = getSensorCounts('displacement')
    # settlement_sensor_counts = getSensorCounts('settlement')
    # vibration_sensor_counts = getSensorCounts('vibration')
    # min_time = (models.StrainData.objects.all().order_by('date_time')[0].date_time).strftime("%Y-%m-%dT%H:%M:%S")
    # max_time = (models.StrainData.objects.all().order_by('-date_time')[0].date_time).strftime("%Y-%m-%dT%H:%M:%S")
    sensor_types = {
        'keys': list(constants.sensor_types.keys()),
        'values': list(constants.sensor_types.values())
    }
    # context.update({'sensor_types':sensor_types, 'strain_sensor_counts': strain_sensor_counts, 'tilt_sensor_counts': tilt_sensor_counts, 'displacement_sensor_counts': displacement_sensor_counts, 'settlement_sensor_counts': settlement_sensor_counts, 'vibration_sensor_counts': vibration_sensor_counts, 'min_time': min_time, 'max_time': max_time})
    context.update({'sensor_types':sensor_types})
    return render(request, 'front/index.html', context)


def importCsv(request):
    if request.method == "POST":
        if 'strain_required' in request.POST.keys():
            models.StrainData.objects.all().delete()
            if request.FILES.get('strain_gauge', None):
                file = request.FILES['strain_gauge']
                tmpname = str(datetime.now().microsecond) + os.path.splitext(str(file))[1]
                fs = FileSystemStorage(settings.MEDIA_ROOT + "csv/", settings.MEDIA_ROOT + "/csv/")
                fs.save(tmpname, file)
                file_name = "csv/" + tmpname

                wb = openpyxl.load_workbook(settings.MEDIA_ROOT + file_name, data_only=True)
                ws = wb.active

                # Extract and clean column names from the Excel file (assuming they are in the first row)
                # column_names = [re.sub(r'[^a-zA-Z0-9_]', '_', str(cell.value)) for cell in ws[1]]
                column_names = [str(cell.value) for cell in ws[1]]

                # Removing Date Time Column
                del column_names[0]

                strain_columns = get_constants('strain')
                for index, column in enumerate(column_names):
                    strain_columns[list(strain_columns.keys())[index]] = column

                f = open("templates/constants/strain_columns.txt", "w+")
                columns = json.dumps(strain_columns)
                f.write(columns)
                f.close()

                # data_list = []

                # Initialize a flag to skip the first row
                skip_first_row = True

                for row in ws.iter_rows(values_only=True):
                    if skip_first_row:
                        skip_first_row = False
                        continue  # Skip the first row
                    if not row[0]:
                        break
                    data = models.StrainData()
                    data.date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                    data.test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                    data.test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                    data.test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                    data.test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                    data.test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                    data.test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                    data.test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                    data.test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                    data.test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                    data.test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                    data.test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                    data.test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                    data.test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                    data.test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                    data.test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                    data.test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                    data.test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                    data.test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                    data.test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                    data.test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                    data.test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                    data.test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                    data.test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                    data.test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                    data.test_method_25=Decimal(row[25]) if len(row) > 25 else None, 
                    data.test_method_26=Decimal(row[26]) if len(row) > 26 else None, 
                    data.test_method_27=Decimal(row[27]) if len(row) > 27 else None, 
                    data.test_method_28=Decimal(row[28]) if len(row) > 28 else None, 
                    data.test_method_29=Decimal(row[29]) if len(row) > 29 else None, 
                    data.test_method_30=Decimal(row[30]) if len(row) > 30 else None, 
                    data.test_method_31=Decimal(row[31]) if len(row) > 31 else None, 
                    data.test_method_32=Decimal(row[32]) if len(row) > 32 else None, 
                    data.test_method_33=Decimal(row[33]) if len(row) > 33 else None, 
                    data.test_method_34=Decimal(row[34]) if len(row) > 34 else None, 
                    data.test_method_35=Decimal(row[35]) if len(row) > 35 else None, 
                    data.test_method_36=Decimal(row[36]) if len(row) > 36 else None, 
                    data.test_method_37=Decimal(row[37]) if len(row) > 37 else None, 
                    data.test_method_38=Decimal(row[38]) if len(row) > 38 else None, 
                    data.test_method_39=Decimal(row[39]) if len(row) > 39 else None, 
                    data.test_method_40=Decimal(row[40]) if len(row) > 40 else None, 
                    data.test_method_41=Decimal(row[41]) if len(row) > 41 else None, 
                    data.test_method_42=Decimal(row[42]) if len(row) > 42 else None
                    data.save()
                #     if len(data_list) > 1000:
                #         models.StrainData.objects.bulk_create(data_list)
                #         data_list = []
                #         data_list.append(models.StrainData(
                #             date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                #             test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                #             test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                #             test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                #             test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                #             test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                #             test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                #             test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                #             test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                #             test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                #             test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                #             test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                #             test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                #             test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                #             test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                #             test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                #             test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                #             test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                #             test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                #             test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                #             test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                #             test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                #             test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                #             test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                #             test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                #             test_method_25=Decimal(row[25]) if len(row) > 25 else None, 
                #             test_method_26=Decimal(row[26]) if len(row) > 26 else None, 
                #             test_method_27=Decimal(row[27]) if len(row) > 27 else None, 
                #             test_method_28=Decimal(row[28]) if len(row) > 28 else None, 
                #             test_method_29=Decimal(row[29]) if len(row) > 29 else None, 
                #             test_method_30=Decimal(row[30]) if len(row) > 30 else None, 
                #             test_method_31=Decimal(row[31]) if len(row) > 31 else None, 
                #             test_method_32=Decimal(row[32]) if len(row) > 32 else None, 
                #             test_method_33=Decimal(row[33]) if len(row) > 33 else None, 
                #             test_method_34=Decimal(row[34]) if len(row) > 34 else None, 
                #             test_method_35=Decimal(row[35]) if len(row) > 35 else None, 
                #             test_method_36=Decimal(row[36]) if len(row) > 36 else None, 
                #             test_method_37=Decimal(row[37]) if len(row) > 37 else None, 
                #             test_method_38=Decimal(row[38]) if len(row) > 38 else None, 
                #             test_method_39=Decimal(row[39]) if len(row) > 39 else None, 
                #             test_method_40=Decimal(row[40]) if len(row) > 40 else None, 
                #             test_method_41=Decimal(row[41]) if len(row) > 41 else None, 
                #             test_method_42=Decimal(row[42]) if len(row) > 42 else None
                #         ))
                #     else:
                #         data_list.append(models.StrainData(
                #             date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                #             test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                #             test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                #             test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                #             test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                #             test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                #             test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                #             test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                #             test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                #             test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                #             test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                #             test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                #             test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                #             test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                #             test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                #             test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                #             test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                #             test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                #             test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                #             test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                #             test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                #             test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                #             test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                #             test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                #             test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                #             test_method_25=Decimal(row[25]) if len(row) > 25 else None, 
                #             test_method_26=Decimal(row[26]) if len(row) > 26 else None, 
                #             test_method_27=Decimal(row[27]) if len(row) > 27 else None, 
                #             test_method_28=Decimal(row[28]) if len(row) > 28 else None, 
                #             test_method_29=Decimal(row[29]) if len(row) > 29 else None, 
                #             test_method_30=Decimal(row[30]) if len(row) > 30 else None, 
                #             test_method_31=Decimal(row[31]) if len(row) > 31 else None, 
                #             test_method_32=Decimal(row[32]) if len(row) > 32 else None, 
                #             test_method_33=Decimal(row[33]) if len(row) > 33 else None, 
                #             test_method_34=Decimal(row[34]) if len(row) > 34 else None, 
                #             test_method_35=Decimal(row[35]) if len(row) > 35 else None, 
                #             test_method_36=Decimal(row[36]) if len(row) > 36 else None, 
                #             test_method_37=Decimal(row[37]) if len(row) > 37 else None, 
                #             test_method_38=Decimal(row[38]) if len(row) > 38 else None, 
                #             test_method_39=Decimal(row[39]) if len(row) > 39 else None, 
                #             test_method_40=Decimal(row[40]) if len(row) > 40 else None, 
                #             test_method_41=Decimal(row[41]) if len(row) > 41 else None, 
                #             test_method_42=Decimal(row[42]) if len(row) > 42 else None
                #         ))
                # models.StrainData.objects.bulk_create(data_list)    
                os.remove(settings.MEDIA_ROOT + file_name)
        if 'tilt_required' in request.POST.keys():
            models.TiltData.objects.all().delete()
            if request.FILES.get('tilt', None):
                file = request.FILES['tilt']
                tmpname = str(datetime.now().microsecond) + os.path.splitext(str(file))[1]
                fs = FileSystemStorage(settings.MEDIA_ROOT + "csv/", settings.MEDIA_ROOT + "/csv/")
                fs.save(tmpname, file)
                file_name = "csv/" + tmpname

                wb = openpyxl.load_workbook(settings.MEDIA_ROOT + file_name, data_only=True)
                ws = wb.active

                # Extract and clean column names from the Excel file (assuming they are in the first row)
                # column_names = [re.sub(r'[^a-zA-Z0-9_]', '_', str(cell.value)) for cell in ws[1]]
                column_names = [str(cell.value) for cell in ws[1]]

                # Removing Date Time Column
                del column_names[0]

                tilt_columns = get_constants('tilt')

                for index, column in enumerate(column_names):
                    tilt_columns[list(tilt_columns.keys())[index]] = column

                f = open("templates/constants/tilt_columns.txt", "w+")
                columns = json.dumps(tilt_columns)
                f.write(columns)
                f.close()

                # data_list = []

                # Initialize a flag to skip the first row
                skip_first_row = True

                for row in ws.iter_rows(values_only=True):
                    if skip_first_row:
                        skip_first_row = False
                        continue  # Skip the first row
                    if not row[0]:
                        break
                    models.TiltData.objects.create(
                        date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                        test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                        test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                        test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                        test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                        test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                        test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                        test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                        test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                        test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                        test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                        test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                        test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                        test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                        test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                        test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                        test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                        test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                        test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                        test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                        test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                        test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                        test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                        test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                        test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                        test_method_25=Decimal(row[25]) if len(row) > 25 else None
                    )
                #     if len(data_list) > 1000:
                #         models.TiltData.objects.bulk_create(data_list)
                #         data_list = []
                #         data_list.append(models.TiltData(
                #             date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                #             test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                #             test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                #             test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                #             test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                #             test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                #             test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                #             test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                #             test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                #             test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                #             test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                #             test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                #             test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                #             test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                #             test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                #             test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                #             test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                #             test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                #             test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                #             test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                #             test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                #             test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                #             test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                #             test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                #             test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                #             test_method_25=Decimal(row[25]) if len(row) > 25 else None
                #         ))
                #     else:
                #         data_list.append(models.TiltData(
                #             date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                #             test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                #             test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                #             test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                #             test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                #             test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                #             test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                #             test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                #             test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                #             test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                #             test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                #             test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                #             test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                #             test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                #             test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                #             test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                #             test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                #             test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                #             test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                #             test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                #             test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                #             test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                #             test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                #             test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                #             test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                #             test_method_25=Decimal(row[25]) if len(row) > 25 else None
                #         ))
                # models.TiltData.objects.bulk_create(data_list)
                os.remove(settings.MEDIA_ROOT + file_name)
        if 'displacement_required' in request.POST.keys():
            models.DisplacementData.objects.all().delete()
            if request.FILES.get('displacement', None):
                file = request.FILES['displacement']
                tmpname = str(datetime.now().microsecond) + os.path.splitext(str(file))[1]
                fs = FileSystemStorage(settings.MEDIA_ROOT + "csv/", settings.MEDIA_ROOT + "/csv/")
                fs.save(tmpname, file)
                file_name = "csv/" + tmpname

                wb = openpyxl.load_workbook(settings.MEDIA_ROOT + file_name, data_only=True)
                ws = wb.active

                # Extract and clean column names from the Excel file (assuming they are in the first row)
                # column_names = [re.sub(r'[^a-zA-Z0-9_]', '_', str(cell.value)) for cell in ws[1]]
                column_names = [str(cell.value) for cell in ws[1]]

                # Removing Date Time Column
                del column_names[0]

                displacement_columns = get_constants('displacement')

                for index, column in enumerate(column_names):
                    displacement_columns[list(displacement_columns.keys())[index]] = column

                f = open("templates/constants/displacement_columns.txt", "w+")
                columns = json.dumps(displacement_columns)
                f.write(columns)
                f.close()

                # data_list = []

                # Initialize a flag to skip the first row
                skip_first_row = True

                for row in ws.iter_rows(values_only=True):
                    if skip_first_row:
                        skip_first_row = False
                        continue  # Skip the first row
                    if not row[0]:
                        break
                    models.DisplacementData.objects.create(
                        date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                        test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                        test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                        test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                        test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                        test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                        test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                        test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                        test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                        test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                        test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                        test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                        test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                        test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                        test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                        test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                        test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                        test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                        test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                        test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                        test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                        test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                        test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                        test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                        test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                        test_method_25=Decimal(row[25]) if len(row) > 25 else None
                    )
                #     if len(data_list) > 1000:
                #         models.DisplacementData.objects.bulk_create(data_list)
                #         data_list = []
                #         data_list.append(models.DisplacementData(
                #             date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                #             test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                #             test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                #             test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                #             test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                #             test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                #             test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                #             test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                #             test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                #             test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                #             test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                #             test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                #             test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                #             test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                #             test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                #             test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                #             test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                #             test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                #             test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                #             test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                #             test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                #             test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                #             test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                #             test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                #             test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                #             test_method_25=Decimal(row[25]) if len(row) > 25 else None
                #         ))
                #     else:
                #         data_list.append(models.DisplacementData(
                #             date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                #             test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                #             test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                #             test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                #             test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                #             test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                #             test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                #             test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                #             test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                #             test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                #             test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                #             test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                #             test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                #             test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                #             test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                #             test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                #             test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                #             test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                #             test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                #             test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                #             test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                #             test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                #             test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                #             test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                #             test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                #             test_method_25=Decimal(row[25]) if len(row) > 25 else None
                #         ))
                # models.DisplacementData.objects.bulk_create(data_list)
                os.remove(settings.MEDIA_ROOT + file_name)
        if 'settlement_required' in request.POST.keys():
            models.SettlementData.objects.all().delete()
            if request.FILES.get('settlement', None):
                file = request.FILES['settlement']
                tmpname = str(datetime.now().microsecond) + os.path.splitext(str(file))[1]
                fs = FileSystemStorage(settings.MEDIA_ROOT + "csv/", settings.MEDIA_ROOT + "/csv/")
                fs.save(tmpname, file)
                file_name = "csv/" + tmpname

                wb = openpyxl.load_workbook(settings.MEDIA_ROOT + file_name, data_only=True)
                ws = wb.active

                # Extract and clean column names from the Excel file (assuming they are in the first row)
                # column_names = [re.sub(r'[^a-zA-Z0-9_]', '_', str(cell.value)) for cell in ws[1]]
                column_names = [str(cell.value) for cell in ws[1]]

                # Removing Date Time Column
                del column_names[0]

                settlement_columns = get_constants('settlement')

                for index, column in enumerate(column_names):
                    settlement_columns[list(settlement_columns.keys())[index]] = column

                f = open("templates/constants/settlement_columns.txt", "w+")
                columns = json.dumps(settlement_columns)
                f.write(columns)
                f.close()

                # data_list = []

                # Initialize a flag to skip the first row
                skip_first_row = True

                for row in ws.iter_rows(values_only=True):
                    if skip_first_row:
                        skip_first_row = False
                        continue  # Skip the first row
                    if not row[0]:
                        break
                    models.DisplacementData.objects.create(
                        date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                        test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                        test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                        test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                        test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                        test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                        test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                        test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                        test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                        test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                        test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                        test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                        test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                        test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                        test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                        test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                        test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                        test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                        test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                        test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                        test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                        test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                        test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                        test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                        test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                        test_method_25=Decimal(row[25]) if len(row) > 25 else None
                    )
                #     if len(data_list) > 1000:
                #         models.SettlementData.objects.bulk_create(data_list)
                #         data_list = []
                #         data_list.append(models.SettlementData(
                #             date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                #             test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                #             test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                #             test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                #             test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                #             test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                #             test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                #             test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                #             test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                #             test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                #             test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                #             test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                #             test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                #             test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                #             test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                #             test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                #             test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                #             test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                #             test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                #             test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                #             test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                #             test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                #             test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                #             test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                #             test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                #             test_method_25=Decimal(row[25]) if len(row) > 25 else None
                #         ))
                #     else:
                #         data_list.append(models.SettlementData(
                #             date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                #             test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                #             test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                #             test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                #             test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                #             test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                #             test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                #             test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                #             test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                #             test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                #             test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                #             test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                #             test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                #             test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                #             test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                #             test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                #             test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                #             test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                #             test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                #             test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                #             test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                #             test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                #             test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                #             test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                #             test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                #             test_method_25=Decimal(row[25]) if len(row) > 25 else None
                #         ))
                # models.SettlementData.objects.bulk_create(data_list)
                os.remove(settings.MEDIA_ROOT + file_name)
        if 'vibration_required' in request.POST.keys():
            models.VibrationData.objects.all().delete()
            if request.FILES.get('vibration', None):
                file = request.FILES['vibration']
                tmpname = str(datetime.now().microsecond) + os.path.splitext(str(file))[1]
                fs = FileSystemStorage(settings.MEDIA_ROOT + "csv/", settings.MEDIA_ROOT + "/csv/")
                fs.save(tmpname, file)
                file_name = "csv/" + tmpname

                wb = openpyxl.load_workbook(settings.MEDIA_ROOT + file_name, data_only=True)
                ws = wb.active

                # Extract and clean column names from the Excel file (assuming they are in the first row)
                # column_names = [re.sub(r'[^a-zA-Z0-9_]', '_', str(cell.value)) for cell in ws[1]]
                column_names = [str(cell.value) for cell in ws[1]]

                # Removing Date Time Column
                del column_names[0]

                vibration_columns = get_constants('vibration')

                for index, column in enumerate(column_names):
                    vibration_columns[list(vibration_columns.keys())[index]] = column

                f = open("templates/constants/vibration_columns.txt", "w+")
                columns = json.dumps(vibration_columns)
                f.write(columns)
                f.close()

                # data_list = []

                # Initialize a flag to skip the first row
                skip_first_row = True

                for row in ws.iter_rows(values_only=True):
                    if skip_first_row:
                        skip_first_row = False
                        continue  # Skip the first row
                    if not row[0]:
                        break
                    models.VibrationData.objects.create(
                        date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                        test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                        test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                        test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                        test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                        test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                        test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                        test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                        test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                        test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                        test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                        test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                        test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                        test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                        test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                        test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                        test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                        test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                        test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                        test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                        test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                        test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                        test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                        test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                        test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                        test_method_25=Decimal(row[25]) if len(row) > 25 else None
                    )
                #     if len(data_list) > 1000:
                #         models.VibrationData.objects.bulk_create(data_list)
                #         data_list = []
                #         data_list.append(models.VibrationData(
                #             date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                #             test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                #             test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                #             test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                #             test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                #             test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                #             test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                #             test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                #             test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                #             test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                #             test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                #             test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                #             test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                #             test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                #             test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                #             test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                #             test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                #             test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                #             test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                #             test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                #             test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                #             test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                #             test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                #             test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                #             test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                #             test_method_25=Decimal(row[25]) if len(row) > 25 else None
                #         ))
                #     else:
                #         data_list.append(models.VibrationData(
                #             date_time=datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S"), 
                #             test_method_1=Decimal(row[1]) if len(row) > 1 else None, 
                #             test_method_2=Decimal(row[2]) if len(row) > 2 else None, 
                #             test_method_3=Decimal(row[3]) if len(row) > 3 else None, 
                #             test_method_4=Decimal(row[4]) if len(row) > 4 else None, 
                #             test_method_5=Decimal(row[5]) if len(row) > 5 else None, 
                #             test_method_6=Decimal(row[6]) if len(row) > 6 else None, 
                #             test_method_7=Decimal(row[7]) if len(row) > 7 else None, 
                #             test_method_8=Decimal(row[8]) if len(row) > 8 else None, 
                #             test_method_9=Decimal(row[9]) if len(row) > 9 else None, 
                #             test_method_10=Decimal(row[10]) if len(row) > 10 else None, 
                #             test_method_11=Decimal(row[11]) if len(row) > 11 else None, 
                #             test_method_12=Decimal(row[12]) if len(row) > 12 else None, 
                #             test_method_13=Decimal(row[13]) if len(row) > 13 else None, 
                #             test_method_14=Decimal(row[14]) if len(row) > 14 else None, 
                #             test_method_15=Decimal(row[15]) if len(row) > 15 else None, 
                #             test_method_16=Decimal(row[16]) if len(row) > 16 else None, 
                #             test_method_17=Decimal(row[17]) if len(row) > 17 else None, 
                #             test_method_18=Decimal(row[18]) if len(row) > 18 else None, 
                #             test_method_19=Decimal(row[19]) if len(row) > 19 else None, 
                #             test_method_20=Decimal(row[20]) if len(row) > 20 else None, 
                #             test_method_21=Decimal(row[21]) if len(row) > 21 else None, 
                #             test_method_22=Decimal(row[22]) if len(row) > 22 else None, 
                #             test_method_23=Decimal(row[23]) if len(row) > 23 else None, 
                #             test_method_24=Decimal(row[24]) if len(row) > 24 else None, 
                #             test_method_25=Decimal(row[25]) if len(row) > 25 else None
                #         ))
                # models.VibrationData.objects.bulk_create(data_list)
                os.remove(settings.MEDIA_ROOT + file_name)
        # Delete all messages by popping them from the list
        try:
            storage = get_messages(request)
            for message in storage:
                message = ''
            storage.used = False
        except:
            pass
        messages.success(request, 'Data Uploaded Successfully.')
        return redirect('index')
    return render(request, 'front/import.html', context)   


def find_key_by_value(dictionary, value_to_find):
    for key, value in dictionary.items():
        if value == value_to_find:
            return key
    # If the value is not found, you can return None or raise an exception.
    return None  # or raise ValueError("Value not found")


def getChartData(request):
    if request.method == "POST":
        sensor_type = request.POST['sensor_type']
        from_time = request.POST['from_time']
        to_time = request.POST['to_time']
        from_miliseconds = int(datetime.fromisoformat(from_time).timestamp() * 1000)
        to_miliseconds = int(datetime.fromisoformat(to_time).timestamp() * 1000)
        if from_miliseconds > to_miliseconds:
            return JsonResponse({
                'code': 503,
                'status': "ERROR",
                'message': "From time should not exceeds To time "
            })
        if sensor_type == 'strain':
            data = models.StrainData.objects.filter(date_time__range=(from_time, to_time)).order_by('id')
            series = []
            sensor_counts = getSensorCounts(sensor_type)
            sensor_names = get_constants(sensor_type)
            columns = {k: v for k, v in sensor_names.items() if not v.startswith('test_method_')}
            dynamic_vars = {}
            for index, element in enumerate(sensor_counts, start=1):
                dynamic_vars[f"test_method_{index}"] = []
            for row_data in data:
                for method in dynamic_vars:
                    dynamic_vars[method].append([int(datetime.fromisoformat(str(row_data.date_time)).timestamp() * 1000), float(getattr(row_data, method))])
            for index, elem in enumerate(request.POST.getlist('method')):
                series.append({'name': columns[elem], 'data': dynamic_vars[elem]})
        if sensor_type == 'tilt':
            data = models.TiltData.objects.filter(date_time__range=(from_time, to_time)).order_by('id')
            series = []
            sensor_counts = getSensorCounts(sensor_type)
            sensor_names = get_constants(sensor_type)
            columns = {k: v for k, v in sensor_names.items() if not v.startswith('test_method_')}
            dynamic_vars = {}
            for index, element in enumerate(sensor_counts, start=1):
                dynamic_vars[f"test_method_{index}"] = []
            for row_data in data:
                for method in dynamic_vars:
                    dynamic_vars[method].append([int(datetime.fromisoformat(str(row_data.date_time)).timestamp() * 1000), float(getattr(row_data, method))])
            for index, elem in enumerate(request.POST.getlist('method')):
                series.append({'name': columns[elem], 'data': dynamic_vars[elem]})
        if sensor_type == 'displacement':
            data = models.DisplacementData.objects.filter(date_time__range=(from_time, to_time)).order_by('id')
            series = []
            sensor_counts = getSensorCounts(sensor_type)
            sensor_names = get_constants(sensor_type)
            columns = {k: v for k, v in sensor_names.items() if not v.startswith('test_method_')}
            dynamic_vars = {}
            for index, element in enumerate(sensor_counts, start=1):
                dynamic_vars[f"test_method_{index}"] = []
            for row_data in data:
                for method in dynamic_vars:
                    dynamic_vars[method].append([int(datetime.fromisoformat(str(row_data.date_time)).timestamp() * 1000), float(getattr(row_data, method))])
            for index, elem in enumerate(request.POST.getlist('method')):
                series.append({'name': columns[elem], 'data': dynamic_vars[elem]})
        if sensor_type == 'settlement':
            data = models.SettlementData.objects.filter(date_time__range=(from_time, to_time)).order_by('id')
            series = []
            sensor_counts = getSensorCounts(sensor_type)
            sensor_names = get_constants(sensor_type)
            columns = {k: v for k, v in sensor_names.items() if not v.startswith('test_method_')}
            dynamic_vars = {}
            for index, element in enumerate(sensor_counts, start=1):
                dynamic_vars[f"test_method_{index}"] = []
            for row_data in data:
                for method in dynamic_vars:
                    dynamic_vars[method].append([int(datetime.fromisoformat(str(row_data.date_time)).timestamp() * 1000), float(getattr(row_data, method))])
            for index, elem in enumerate(request.POST.getlist('method')):
                series.append({'name': columns[elem], 'data': dynamic_vars[elem]})
        if sensor_type == 'vibration':
            data = models.VibrationData.objects.filter(date_time__range=(from_time, to_time)).order_by('id')
            series = []
            sensor_counts = getSensorCounts(sensor_type)
            sensor_names = get_constants(sensor_type)
            columns = {k: v for k, v in sensor_names.items() if not v.startswith('test_method_')}
            dynamic_vars = {}
            for index, element in enumerate(sensor_counts, start=1):
                dynamic_vars[f"test_method_{index}"] = []
            for row_data in data:
                for method in dynamic_vars:
                    dynamic_vars[method].append([int(datetime.fromisoformat(str(row_data.date_time)).timestamp() * 1000), float(getattr(row_data, method))])
            for index, elem in enumerate(request.POST.getlist('method')):
                series.append({'name': columns[elem], 'data': dynamic_vars[elem]})
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