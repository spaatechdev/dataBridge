import environ
import math
import json
from rest_framework.permissions import IsAuthenticated

from . import models
from datetime import datetime

from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.db import transaction
from django.db.models import Q

env = environ.Env()
environ.Env.read_env()

class CustomPaginator:
    def __init__(self, items, per_page):
        self.items = items
        self.per_page = per_page

    def get_page(self, page_number):
        page_number = int(page_number)  # Convert to integer
        start = (page_number - 1) * self.per_page
        end = start + self.per_page
        page_items = self.items[start:end]
        return page_items

    def get_total_pages(self):
        return math.ceil(len(self.items) / self.per_page)


@api_view(['GET'])
def sensorTypeList(request):
    context = {}
    id = request.GET.get('id', None)
    find_all = request.GET.get('find_all', None)
    keyword = request.GET.get('keyword', None)
    if id is not None and id != "":
        sensorType = list(models.SensorType.objects.filter(pk=id)[:1].values('pk', 'name'))
        context.update({
            'status': 200,
            'message': "Sensor Type Fetched Successfully.",
            'page_items': sensorType,
        })
    else:
        if keyword is not None and keyword != "":
            sensorTypes = list(models.SensorType.objects.filter(
                name__icontains=keyword).values('pk', 'name'))
        else:
            sensorTypes = list(models.SensorType.objects.all().values('pk', 'name'))

        if find_all is not None and int(find_all) == 1:
            context.update({
                'status': 200,
                'message': "Sensor Types Fetched Successfully.",
                'page_items': sensorTypes,
            })
            return JsonResponse(context)
        per_page = int(env("PER_PAGE_DATA"))
        button_to_show = int(env("PER_PAGE_PAGINATION_BUTTON"))
        current_page = request.GET.get('current_page', 1)

        paginator = CustomPaginator(sensorTypes, per_page)
        page_items = paginator.get_page(current_page)
        total_pages = paginator.get_total_pages()

        context.update({
            'status': 200,
            'message': "Sensor Types Fetched Successfully.",
            'page_items': page_items,
            'total_pages': total_pages,
            'per_page': per_page,
            'current_page': int(current_page),
            'button_to_show': int(button_to_show),
        })
    return JsonResponse(context)


@api_view(['POST'])
def sensorTypeAdd(request):
    context = {}
    if not request.POST['name']:
        context.update({
            'status': 531,
            'message': "Name has not been provided."
        })
        return JsonResponse(context)
    exist_data = models.SensorType.objects.filter(
        name=request.POST['name']).all()
    if len(exist_data) > 0:
        context.update({
            'status': 532,
            'message': "Sensor Type with this name already exists.",
        })
        return JsonResponse(context)
    try:
        with transaction.atomic():
            sensorType = models.SensorType()
            sensorType.name = request.POST['name']
            sensorType.save()
        transaction.commit()
        context.update({
            'status': 200,
            'message': "Sensor Type Created Successfully."
        })
    except Exception:
        context.update({
            'status': 533,
            'message': "Something Went Wrong. Please Try Again."
        })
        transaction.rollback()
    return JsonResponse(context)


@api_view(['POST'])
def sensorTypeEdit(request):
    context = {}
    if not request.POST['name']:
        context.update({
            'status': 534,
            'message': "Name has not been provided."
        })
        return JsonResponse(context)
    exist_data = models.SensorType.objects.filter(
        name=request.POST['name']).exclude(pk=request.POST['id']).all()
    if len(exist_data) > 0:
        context.update({
            'status': 535,
            'message': "Sensor Type with this name already exists.",
        })
        return JsonResponse(context)
    try:
        with transaction.atomic():
            sensorType = models.SensorType.objects.get(pk=request.POST['id'])
            sensorType.name = request.POST['name']
            sensorType.updated_at = datetime.now()
            sensorType.save()
        transaction.commit()
        context.update({
            'status': 200,
            'message': "Sensor Type Updated Successfully."
        })
    except Exception:
        context.update({
            'status': 536,
            'message': "Something Went Wrong. Please Try Again."
        })
        transaction.rollback()
    return JsonResponse(context)


@api_view(['POST'])
def sensorTypeDelete(request):
    context = {}
    sensorType = models.SensorType.objects.get(pk=request.POST['id'])
    try:
        with transaction.atomic():
            sensorType.delete()
        transaction.commit()
        context.update({
            'status': 200,
            'message': "Sensor Type Deleted Successfully."
        })
    except Exception:
        context.update({
            'status': 537,
            'message': "Something Went Wrong. Please Try Again."
        })
        transaction.rollback()
    return JsonResponse(context)


@api_view(['GET'])
def sensorList(request):
    print(request)
    context = {}
    id = request.GET.get('id', None)
    sensor_type_id = request.GET.get('sensor_type_id', None)
    section_id = request.GET.get('section_id', None)
    find_all = request.GET.get('find_all', None)
    keyword = request.GET.get('keyword', None)
    if id is not None and id != "":
        sensor = list(models.Sensor.objects.filter(pk=id)[:1].values(
            'pk', 'name', 'sensor_type_id', 'sensor_type__name', 'max', 'min'))
        context.update({
            'status': 200,
            'message': "Sensor Fetched Successfully.",
            'page_items': sensor,
        })
    elif sensor_type_id is not None:
        available_sensors=[]
        chosen_sensors=[]
        if section_id is not None and section_id!='':
            sensor_id_list = list(models.Section_Sensor_Mapping.objects.filter(section_id=section_id).values_list("sensor_id", flat=True))
            available_sensors = list(models.Sensor.objects.filter(sensor_type_id=sensor_type_id).exclude(pk__in=sensor_id_list).values('pk', 'name'))
            chosen_sensors = list(models.Sensor.objects.filter(sensor_type_id=sensor_type_id, pk__in=sensor_id_list).values('pk', 'name'))
        else:
            available_sensors = list(models.Sensor.objects.filter(sensor_type_id=sensor_type_id).values('pk', 'name'))

        min_time = (models.Sensor_Data.objects.filter(section_sensor_mapping__sensor__sensor_type__id=sensor_type_id).order_by('time_stamp__date_time').first().time_stamp.date_time
                    ).strftime("%Y-%m-%dT%H:%M:%S")

        max_time = (models.Sensor_Data.objects.filter(section_sensor_mapping__sensor__sensor_type__id=sensor_type_id).order_by('-time_stamp__date_time').first().time_stamp.date_time
                    ).strftime("%Y-%m-%dT%H:%M:%S")

        context.update({
            'status': 200,
            'message': "Sensor Fetched Successfully.",
            'available_sensors': available_sensors,
            'chosen_sensors': chosen_sensors,
            'min_time': min_time,
            'max_time': max_time,
        })
    else:
        if keyword is not None and keyword != "":
            sensors = list(models.Sensor.objects.filter(
                Q(name__icontains=keyword) | Q(sensor_type__name__icontains=keyword)).all().values(
                        'pk', 'name', 'sensor_type_id', 'sensor_type__name', 'max', 'min'
                    )
                )
        else:
            sensors = list(models.Sensor.objects.all().values(
                'pk', 'name', 'sensor_type_id', 'sensor_type__name', 'max', 'min'))
        if find_all is not None and int(find_all) == 1:
            context.update({
                'status': 200,
                'message': "Sensors Fetched Successfully.",
                'page_items': sensors,
            })
            return JsonResponse(context)

        per_page = int(env("PER_PAGE_DATA"))
        button_to_show = int(env("PER_PAGE_PAGINATION_BUTTON"))
        current_page = request.GET.get('current_page', 1)

        paginator = CustomPaginator(sensors, per_page)
        page_items = paginator.get_page(current_page)
        total_pages = paginator.get_total_pages()

        context.update({
            'status': 200,
            'message': "Sensors Fetched Successfully.",
            'page_items': page_items,
            'total_pages': total_pages,
            'per_page': per_page,
            'current_page': int(current_page),
            'button_to_show': int(button_to_show),
        })
    return JsonResponse(context)


@api_view(['POST'])
def sensorAdd(request):
    context = {}
    if not request.POST['name'] or not request.POST['sensor_type_id']:
        context.update({
            'status': 538,
            'message': "Name/Sensor Types has not been provided."
        })
        return JsonResponse(context)
    exist_data = models.Sensor.objects.filter(
        name=request.POST['name'], sensor_type_id=request.POST['sensor_type_id']).all()
    if len(exist_data) > 0:
        context.update({
            'status': 539,
            'message': "Sensor with this name and sensor type already exists.",
        })
        return JsonResponse(context)
    try:
        with transaction.atomic():
            sensor = models.Sensor()
            sensor.name = request.POST['name']
            sensor.sensor_type_id = request.POST['sensor_type_id']
            if request.POST['max']:
                sensor.max = request.POST['max']
            if request.POST['min']:
                sensor.min = request.POST['min']
            sensor.save()
        transaction.commit()
        context.update({
            'status': 200,
            'message': "Sensor Created Successfully."
        })
    except Exception:
        context.update({
            'status': 540,
            'message': "Something Went Wrong. Please Try Again."
        })
        transaction.rollback()
    return JsonResponse(context)


@api_view(['POST'])
def sensorEdit(request):
    context = {}
    if not request.POST['name'] or not request.POST['sensor_type_id'] :
        context.update({
            'status': 541,
            'message': "Name/Sensor Type has not been provided."
        })
        return JsonResponse(context)
    exist_data = models.Sensor.objects.filter(
        name=request.POST['name'], sensor_type_id=request.POST['sensor_type_id']).exclude(pk=request.POST['id']).all()
    if len(exist_data) > 0:
        context.update({
            'status': 542,
            'message': "Sensor with this name and sensor type already exists.",
        })
        return JsonResponse(context)
    try:
        with transaction.atomic():
            sensor = models.Sensor.objects.get(pk=request.POST['id'])
            sensor.name = request.POST['name']
            sensor.sensor_type_id = request.POST['sensor_type_id']
            if request.POST['max']:
                sensor.max = request.POST['max']
            if request.POST['min']:
                sensor.min = request.POST['min']
            sensor.updated_at = datetime.now()
            sensor.save()
        transaction.commit()
        context.update({
            'status': 200,
            'message': "Sensor Updated Successfully."
        })
    except Exception:
        context.update({
            'status': 543,
            'message': "Something Went Wrong. Please Try Again."
        })
        transaction.rollback()
    return JsonResponse(context)


@api_view(['POST'])
def sensorDelete(request):
    context = {}
    sensor = models.Sensor.objects.get(pk=request.POST['id'])
    try:
        with transaction.atomic():
            sensor.delete()
        transaction.commit()
        context.update({
            'status': 200,
            'message': "Sensor Deleted Successfully."
        })
    except Exception:
        context.update({
            'status': 544,
            'message': "Something Went Wrong. Please Try Again."
        })
        transaction.rollback()
    return JsonResponse(context)


@api_view(['GET'])
def sectionList(request):
    context = {}
    id = request.GET.get('id', None)
    find_all = request.GET.get('find_all', None)
    keyword = request.GET.get('keyword', None)
    if id is not None and id != "":
        section = list(models.Section.objects.filter(pk=id)[:1].values('pk', 'name'))
        context.update({
            'status': 200,
            'message': "Section Fetched Successfully.",
            'page_items': section,
        })
    else:
        if keyword is not None and keyword != "":
            sections = list(models.Section.objects.filter(
                name__icontains=keyword).values('pk', 'name'))
        else:
            sections = list(models.Section.objects.all().values('pk', 'name'))

        if find_all is not None and int(find_all) == 1:
            context.update({
                'status': 200,
                'message': "Sections Fetched Successfully.",
                'page_items': sections,
            })
            return JsonResponse(context)
        per_page = int(env("PER_PAGE_DATA"))
        button_to_show = int(env("PER_PAGE_PAGINATION_BUTTON"))
        current_page = request.GET.get('current_page', 1)

        paginator = CustomPaginator(sections, per_page)
        page_items = paginator.get_page(current_page)
        total_pages = paginator.get_total_pages()

        context.update({
            'status': 200,
            'message': "Sections Fetched Successfully.",
            'page_items': page_items,
            'total_pages': total_pages,
            'per_page': per_page,
            'current_page': int(current_page),
            'button_to_show': int(button_to_show),
        })
    return JsonResponse(context)


@api_view(['POST'])
def sectionAdd(request):
    context = {}
    if not request.POST['name']:
        context.update({
            'status': 531,
            'message': "Name has not been provided."
        })
        return JsonResponse(context)
    exist_data = models.Section.objects.filter(
        name=request.POST['name']).all()
    if len(exist_data) > 0:
        context.update({
            'status': 532,
            'message': "Section with this name already exists.",
        })
        return JsonResponse(context)
    try:
        with transaction.atomic():
            section = models.Section()
            section.name = request.POST['name']
            section.save()
        transaction.commit()
        context.update({
            'status': 200,
            'message': "Section Created Successfully."
        })
    except Exception:
        context.update({
            'status': 533,
            'message': "Something Went Wrong. Please Try Again."
        })
        transaction.rollback()
    return JsonResponse(context)


@api_view(['POST'])
def sectionEdit(request):
    context = {}
    if not request.POST['name']:
        context.update({
            'status': 534,
            'message': "Name has not been provided."
        })
        return JsonResponse(context)
    exist_data = models.Section.objects.filter(
        name=request.POST['name']).exclude(pk=request.POST['id']).all()
    if len(exist_data) > 0:
        context.update({
            'status': 535,
            'message': "Section with this name already exists.",
        })
        return JsonResponse(context)
    try:
        with transaction.atomic():
            section = models.Section.objects.get(pk=request.POST['id'])
            section.name = request.POST['name']
            section.updated_at = datetime.now()
            section.save()
        transaction.commit()
        context.update({
            'status': 200,
            'message': "Section Updated Successfully."
        })
    except Exception:
        context.update({
            'status': 536,
            'message': "Something Went Wrong. Please Try Again."
        })
        transaction.rollback()
    return JsonResponse(context)


@api_view(['POST'])
def sectionDelete(request):
    context = {}
    section = models.Section.objects.get(pk=request.POST['id'])
    try:
        with transaction.atomic():
            section.delete()
        transaction.commit()
        context.update({
            'status': 200,
            'message': "Section Deleted Successfully."
        })
    except Exception:
        context.update({
            'status': 537,
            'message': "Something Went Wrong. Please Try Again."
        })
        transaction.rollback()
    return JsonResponse(context)


@api_view(['GET'])
def sectionSensorMappingList(request):
    context = {}
    id = request.GET.get('id', None)
    find_all = request.GET.get('find_all', None)
    keyword = request.GET.get('keyword', None)
    if id is not None and id != "":
        sectionSensorMapping = list(models.Section_Sensor_Mapping.objects.filter(pk=id)[:1].values(
            'pk', 'section__name', 'sensor__name'))
        context.update({
            'status': 200,
            'message': "Section Sensor Mapping Fetched Successfully.",
            'page_items': sectionSensorMapping,
        })
    else:
        if keyword is not None and keyword != "":
            SectionSensorMappings = list(models.Section_Sensor_Mapping.objects.filter(
                Q(section__name__icontains=keyword) | Q(sensor__name__icontains=keyword)).all().values(
                        'pk', 'section__name', 'sensor__name'))
        else:
            SectionSensorMappings = list(models.Section_Sensor_Mapping.objects.all().values(
                'pk', 'section__name', 'sensor__name'))
        if find_all is not None and int(find_all) == 1:
            context.update({
                'status': 200,
                'message': "Section Sensor Mappings Fetched Successfully.",
                'page_items': SectionSensorMappings,
            })
            return JsonResponse(context)

        per_page = int(env("PER_PAGE_DATA"))
        button_to_show = int(env("PER_PAGE_PAGINATION_BUTTON"))
        current_page = request.GET.get('current_page', 1)

        paginator = CustomPaginator(SectionSensorMappings, per_page)
        page_items = paginator.get_page(current_page)
        total_pages = paginator.get_total_pages()

        context.update({
            'status': 200,
            'message': "Section Sensor Mappings Fetched Successfully.",
            'page_items': page_items,
            'total_pages': total_pages,
            'per_page': per_page,
            'current_page': int(current_page),
            'button_to_show': int(button_to_show),
        })
    return JsonResponse(context)


@api_view(['POST'])
def sectionSensorMappingAdd(request):
    context = {}
    if not request.POST['section_id'] or not request.POST['sensor_type_id']:
        context.update({
            'status': 531,
            'message': "Section id or Sensor ids has not been provided."
        })
        return JsonResponse(context)
    try:
        with transaction.atomic():
            section_id=request.POST['section_id']
            sensor_type_id = request.POST['sensor_type_id']
            section_sensor_mappings=[]
            for sensor_id in request.POST.getlist('chosen_sensors'):
                if not models.Section_Sensor_Mapping.objects.filter(section_id=section_id, sensor_id=sensor_id).exists():
                    section_sensor_mapping=models.Section_Sensor_Mapping()
                    section_sensor_mapping.section_id=section_id
                    section_sensor_mapping.sensor_id = sensor_id
                    section_sensor_mapping.save()
            # models.Section_Sensor_Mapping.objects.bulk_create(section_sensor_mappings)
            # models.Section_Sensor_Mapping.objects.filter(
            #     section_id=section_id, sensor__sensor_type_id=sensor_type_id).exclude(
            #     sensor_id__in=request.POST.getlist('chosen_sensors').delete()
            # )
        transaction.commit()
        context.update({
            'status': 200,
            'message': "Section Sensor Mapping Created Successfully."
        })
    except Exception:
        context.update({
            'status': 533,
            'message': "Something Went Wrong. Please Try Again."
        })
        transaction.rollback()
    return JsonResponse(context)


@api_view(['POST'])
def sectionSensorMappingDelete(request):
    context = {}
    sectionSensorMapping = models.Section_Sensor_Mapping.objects.get(pk=request.POST['id'])
    try:
        with transaction.atomic():
            sectionSensorMapping.delete()
        transaction.commit()
        context.update({
            'status': 200,
            'message': "Section Sensor Mapping Deleted Successfully."
        })
    except Exception:
        context.update({
            'status': 537,
            'message': "Something Went Wrong. Please Try Again."
        })
        transaction.rollback()
    return JsonResponse(context)


@api_view(['GET'])
def upload(request):
    context = {}
    sensors = []

    if len(models.SensorType.objects.all())==4:
        with open('templates/constants/strain_columns.txt') as f:
            data = f.read()
        strain_columns = json.loads(data)

        for name in list(strain_columns.values()):
            if not models.Sensor.objects.filter(name=name, sensor_type_id=models.SensorType.objects.get(name="Strain").id).exists():
                sensors.append(
                    models.Sensor(
                        name=name,
                        sensor_type_id=models.SensorType.objects.get(name="Strain").id
                    )
                )

        with open('templates/constants/tilt_columns.txt') as f:
            data = f.read()
        tilt_columns = json.loads(data)

        for name in list(tilt_columns.values()):
            if not models.Sensor.objects.filter(name=name, sensor_type_id=models.SensorType.objects.get(name="Tilt").id).exists():
                sensors.append(
                    models.Sensor(
                        name=name,
                        sensor_type_id=models.SensorType.objects.get(name="Tilt").id
                    )
                )

        with open('templates/constants/settlement_p_columns.txt') as f:
            data = f.read()
        settlement_p_columns = json.loads(data)

        for name in list(settlement_p_columns.values()):
            if not models.Sensor.objects.filter(name=name, sensor_type_id=models.SensorType.objects.get(name="Settlement(P)").id).exists():
                sensors.append(
                    models.Sensor(
                        name=name,
                        sensor_type_id=models.SensorType.objects.get(name="Settlement(P)").id
                    )
                )

        with open('templates/constants/settlement_f_columns.txt') as f:
            data = f.read()
        settlement_f_columns = json.loads(data)

        for name in list(settlement_f_columns.values()):
            if not models.Sensor.objects.filter(name=name, sensor_type_id=models.SensorType.objects.get(name="Settlement(F)").id).exists():
                sensors.append(
                    models.Sensor(
                        name=name,
                        sensor_type_id=models.SensorType.objects.get(name="Settlement(F)").id
                    )
                )

    models.Sensor.objects.bulk_create(sensors)
    context.update({
        'status': 200,
        'message': "Uploaded Successfully."
    })
    return JsonResponse(context)