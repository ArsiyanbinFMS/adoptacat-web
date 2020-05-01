from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage,name="home"),
    path('catlist/', views.catlist,name="catlist"),
    path('adoptedcat/', views.adoptedcat,name="adoptedcat"),
    path('/adopted_info/<id>/', views.adoptedinfo, name='adopted_info'),
    #path('/adopted_form/<id>/', views.adoptedform, name='adoptedform'),
    path('mycatlist/', views.mycatlist,name="mycatlist"),
    path('myrequest_list/', views.myrequestlist, name='myrequest_list'),
    path('addcat/', views.addcat_page,name="addcat"),
    path('/catinfo/<id>/', views.catinfo, name='catinfo'),
    path('/delete/<cat_id>', views.delete, name='delete'),
    path('/edit/<id>/', views.edit, name='edit'),
    
    path('/request_list/<id>/', views.requestlist, name='request_list'),
    path('/request_info/<id>/', views.requestinfo, name='request_info'),
]