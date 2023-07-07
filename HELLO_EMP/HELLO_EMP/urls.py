
from django.contrib import admin
from django.urls import path
from HELLO_EMP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.emp_list),
    path('emp_list', views.emp_list),
    path('emp_detail', views.emp_detail),
    path('emp_mod', views.emp_mod),
    path('emp_mod_act', views.emp_mod_act),
    path('emp_add', views.emp_add),
    path('emp_add_act', views.emp_add_act),
    path('emp_del_act', views.emp_del_act),
    
    path('emp_list_fake', views.emp_list_fake),
]
