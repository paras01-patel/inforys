"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name='landing'),
    path('login/',views.login,name='login'),
    path('admindashboard',views.admindashboard,name='admindashboard'),
    path('logout',views.logout,name='logout'),
    # path('Department',views.Department,name='Department'),
    path('add_employee/',views.add_employee,name='add_employee'),
    path('add',views.add,name='add'),
    path('all_employee/',views.all_employee,name='all_employee'),
    path('add_department/',views.add_department,name='add_department'),
    path('add_d',views.add_d,name="add_d"),
    path('all_department',views.all_department,name='all_department'),
    path('userpanel/',views.userpanel,name='userpanel'),
    
    # userpanel
     path('userpanel/',views.userpanel,name='userpanel'),
    path('submit_q/',views.submit_q,name='submit_q'),
    path('show_q/',views.show_q,name='show_q'),
    path('all_q/',views.all_q,name='all_q'),
    path('pending/',views.pending,name='pending'),
    path('pending_q/',views.pending_q,name='pending_q'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('delete/<int:pk>',views.delete,name='delete')
    
    
    
    
    

]
