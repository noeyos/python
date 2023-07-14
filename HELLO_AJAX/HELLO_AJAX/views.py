from django.shortcuts import render
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from HELLO_AJAX.dao_emp import DaoEmp

def emp(request):
    return render(request, "emp.html")

@csrf_exempt
def ajax(request):
    data = json.loads(request.body)
    print(data['e_id'])
    context = {
        'result': data,
    }
    return JsonResponse(context)

@csrf_exempt
def emp_list(request):
    de = DaoEmp()
    emps = de.selectList()
    return JsonResponse({'list' : emps})

@csrf_exempt
def emp_detail(request):
    param = json.loads(request.body)
    e_id = param['e_id']
    print(param['e_id'])
    de = DaoEmp()
    vo = de.selectOne(e_id)
    return JsonResponse({'vo' : vo})

@csrf_exempt
def emp_add(request):
    vo = json.loads(request.body)
    e_id = vo['e_id']
    e_name = vo['e_name']
    gen = vo['gen']
    addr = vo['addr']
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    return JsonResponse({'cnt' : cnt})

@csrf_exempt
def emp_mod(request):
    vo = json.loads(request.body)
    e_id = vo['e_id']
    e_name = vo['e_name']
    gen = vo['gen']
    addr = vo['addr']
    de = DaoEmp()
    cnt = de.update(e_name, gen, addr, e_id)
    return JsonResponse({'cnt' : cnt})

@csrf_exempt
def emp_del(request):
    vo = json.loads(request.body)
    e_id = vo['e_id']
    de = DaoEmp()
    cnt = de.delete(e_id)
    return JsonResponse({'cnt' : cnt})

