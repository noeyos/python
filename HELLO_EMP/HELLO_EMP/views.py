from django.shortcuts import render
import pymysql
from HELLO_EMP.dao_emp import DaoEmp
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def emp_list(request):
    de = DaoEmp()
    emps = de.selectList()
    return render(request, "emp_list.html", {'emp' : emps})

def emp_list_fake(request):
    de = DaoEmp()
    emps = de.selectList()
    return render(request, "emp_list_fake.html", {'emp' : emps})

def emp_detail(request):
    id = request.GET.get('e_id')
    de = DaoEmp()
    emps = de.selectOne(id)
    return render(request, "emp_detail.html", {'emp':emps})

def emp_mod(request):
    id = request.GET.get('e_id')
    de = DaoEmp()
    emps = de.selectOne(id)
    return render(request, "emp_mod.html", {'emp':emps})

def emp_mod_act(request):
    e_id = request.POST.get('e_id')
    e_name = request.POST.get('e_name')
    gen = request.POST.get('gen')
    addr = request.POST.get('addr')
    print(e_id)
    de = DaoEmp()
    cnt = de.update(e_name, gen, addr, e_id)
    return render(request, "emp_mod_act.html", {'cnt' : cnt})
#cnt가 1이면 list 그렇지 않으면 emp_mod로 historyback

def emp_add(request):
    return render(request, "emp_add.html")
    
def emp_add_act(request):
    e_id = request.POST.get('e_id')
    e_name = request.POST.get('e_name')
    gen = request.POST.get('gen')
    addr = request.POST.get('addr')
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    return render(request, "emp_add_act.html", {'cnt' : cnt})

@csrf_exempt
def emp_del_act(request):
    e_id = request.POST.get('e_id')
    de = DaoEmp()
    cnt = de.delete(e_id)
    return render(request,"emp_del_act.html", {'cnt':cnt})
    