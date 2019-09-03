from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


from .models import Msg
import json


@csrf_exempt
@require_http_methods(['POST'])
def write_msg(request):
    try:
        data = json.loads(request.body)
        new_msg = Msg(
            sender=data["sender"],
            receiver=data["receiver"],
            subject=data["subject"],
            message=data["message"],
            been_read=data["been_read"],
            creation_date=datetime.now())

        new_msg.save()
        return HttpResponse("message was sent successfully")
    except Exception as error:
        return HttpResponse(f"opps, ERROR:{error}")


@require_http_methods(['GET'])
def read_all_msg(request):
    try:
        name = request.GET.get("name")
        data = list(Msg.objects.filter(receiver=name).values())
        return JsonResponse({"all": data})
    except Exception as error:
        return HttpResponse(f"opps, ERROR:{error}")


@csrf_exempt
@require_http_methods(['PUT'])
def read_msg(request):
    try:
        data = json.loads(request.body)
        Msg_to_change = Msg.objects.get(id=data["id"])
        Msg_to_change.been_read = True
        Msg_to_change.save()
        listed_data = list(Msg.objects.filter(id=data["id"]).values())
        print(listed_data)
        return JsonResponse({"MSG": listed_data})
    except Exception as error:
        return HttpResponse(f"opps, ERROR:{error}")


@require_http_methods(['GET'])
def read_all_unread_msg(request):
    try:
        name = request.GET.get("name")
        data = Msg.objects.filter(receiver=name).values()
        filter_data = list(data.filter(been_read=False))
        return JsonResponse({"all": filter_data})
    except Exception as error:
        return HttpResponse(f"opps, ERROR:{error}")


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_msg(request):
    try:
        data = json.loads(request.body)
        applyer = data["applyer"]
        Msg_to_delete = Msg.objects.get(id=data["id"])
        if applyer == Msg_to_delete.receiver or applyer == Msg_to_delete.sender:
            Msg_to_delete.delete()
        else:
            return JsonResponse("ERROR:not your message to delete...", safe=False)
        return JsonResponse("message was deleted", safe=False)
    except Exception as error:
        return HttpResponse(f"opps, ERROR:{error}")
