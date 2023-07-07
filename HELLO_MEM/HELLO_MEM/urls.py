
from django.contrib import admin
from django.urls import path
from HELLO_MEM import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mem_list),
    path('mem_list', views.mem_list),
    path('mem_add', views.mem_add),
    path('mem_add_act', views.mem_add_act),
    path('mem_detail', views.mem_detail),
    path('mem_mod', views.mem_mod),
    path('mem_mod_act', views.mem_mod_act),
    path('mem_del_act', views.mem_del_act),
]
