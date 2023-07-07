
from django.contrib import admin
from django.urls import path
from HELLO_DJANGO import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('param', views.param),
    path('post', views.post),
    path('forw', views.forw),
]
