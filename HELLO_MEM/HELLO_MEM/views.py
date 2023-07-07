from HELLO_MEM.dao_mem import DaoMem
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def mem_list(request):
    dm = DaoMem()
    mems = dm.selectList()
    return render(request, "mem_list.html", {'mem':mems})

def mem_add(request):
    return render(request, "mem_add.html")

def mem_add_act(request):
    m_id = request.POST.get('m_id')
    m_nm = request.POST.get('m_nm')
    tel = request.POST.get('tel')
    address = request.POST.get('address')
    dm = DaoMem()
    cnt = dm.insert(m_id, m_nm, tel, address)
    return render(request, "mem_add_act.html", {'cnt' : cnt})

def mem_detail(request):
    m_id = request.GET.get('m_id')
    dm = DaoMem()
    mems = dm.selectOne(m_id)
    return render(request, "mem_detail.html", {'mem':mems})

def mem_mod(request):
    m_id = request.GET.get('m_id')
    dm = DaoMem()
    mems = dm.selectOne(m_id)
    return render(request, "mem_mod.html", {'mem':mems})

def mem_mod_act(request):
    m_id = request.POST.get('m_id')
    m_nm = request.POST.get('m_nm')
    tel = request.POST.get('tel')
    address = request.POST.get('address')
    print(m_id)
    dm = DaoMem()
    cnt = dm.update(m_nm, tel, address, m_id)
    return render(request, "mem_mod_act.html", {'cnt' : cnt})

@csrf_exempt
def mem_del_act(request):
    m_id = request.POST.get('m_id')
    dm = DaoMem()
    cnt = dm.delete(m_id)
    return render(request,"mem_del_act.html", {'cnt':cnt})