
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin', admin.site.urls),
    path('',include('emp_app.urls')),
    path('employees',include('django.contrib.auth.urls')),
    path('employees',include('employees.urls')),
]
