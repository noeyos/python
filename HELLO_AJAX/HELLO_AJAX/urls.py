
from django.contrib import admin
from django.urls import path
from HELLO_AJAX import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.emp),
    path('emp', views.emp),
    path('ajax', views.ajax),
    path('emp_list', views.emp_list),
    path('emp_detail', views.emp_detail),
    path('emp_add', views.emp_add),
    path('emp_mod', views.emp_mod),
    path('emp_del', views.emp_del),
]
