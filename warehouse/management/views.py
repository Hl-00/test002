from django.core.serializers import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from management.models import UserInfo, meter, inventory


def user_class(request):
    user = UserInfo.objects.values().all()
    user_list = list(user)
    return JsonResponse(user_list , safe=False)


def electric_meter(request):
    ammeter_info = meter.objects.values().all()
    return JsonResponse(list(ammeter_info) , safe=False)


# 删除电表信息
def del_info(request):
    if request.method == 'POST':
        postBody = json.loads(request.body)
        # print(postBody['id'])
        meter.objects.get(id = postBody['id']).delete()
        return JsonResponse('200', safe=False)
    else:
        return JsonResponse('请求错误：get')


# 添加电表信息
def add_info(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        meter.objects.create(
            id=postBody['id'],
            start_numbering=postBody['start_numbering'],
            stop_numbering=postBody['stop_numbering'],
            model=postBody['model'],
            factory=postBody['factory'],
            date=postBody['date'],
            years=postBody['years'],
            cycle=postBody['cycle'],
            appraiser=postBody['appraiser'],
            appraisal_date=postBody['appraisal_date']
        ).save()

        # print(postBody)
        return  JsonResponse('200', safe=False)
    else:
        return JsonResponse('请求错误：get')


# 编辑电表信息
def edit_info(request):
    if request.method == 'POST':
        postBody = json.loads(request.body)
        # print(postBody['id'])
        meter.objects.filter(id=postBody['id']).update(
            start_numbering=postBody['start_numbering'],
            stop_numbering=postBody['stop_numbering'],
            model=postBody['model'],
            factory=postBody['factory'],
            date=postBody['date'],
            years=postBody['years'],
            cycle=postBody['cycle'],
            appraiser=postBody['appraiser'],
            appraisal_date=postBody['appraisal_date']
        )
        return JsonResponse('200', safe=False)
    else:
        return JsonResponse('请求错误：get')


# 删除人员信息
def del_user_info(request):
    if request.method == 'POST':
        postBody = json.loads(request.body)
        print(postBody['id'])
        UserInfo.objects.get(id = postBody['id']).delete()
        return JsonResponse('200', safe=False)
    else:
        return JsonResponse('请求错误：get')


# 编辑人员信息
def edit_user_info(request):
    if request.method == 'POST':
        postBody = json.loads(request.body)
        print(postBody['id'])
        UserInfo.objects.filter(id=postBody['id']).update(
            username=postBody['username'],
            password=postBody['password'],
            root=postBody['root']
        )
        return JsonResponse('200', safe=False)
    else:
        return JsonResponse('请求错误：get')


# 添加人员信息
def add_user_info(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        print(postBody)
        UserInfo.objects.create(
            username=postBody['name'],
            password=postBody['password'],
            root=postBody['root']
        ).save()

        # print(postBody)
        return  JsonResponse('200', safe=False)
    else:
        return JsonResponse('请求错误：get')


# 出库列表信息
def inventory_info(request):
    user = inventory.objects.values().all()
    user_list = list(user)
    return JsonResponse(user_list , safe=False)


# 删除出库信息
def del_invent_info(request):
    if request.method == 'POST':
        # postBody = json.loads(request.body)
        # print(postBody['id'])
        # inventory.objects.get(id = postBody['id']).delete()
        return JsonResponse('200', safe=False)
    else:
        return JsonResponse('请求错误：get')