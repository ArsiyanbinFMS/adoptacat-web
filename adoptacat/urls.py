
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path ,include
from django.conf import settings 
from accounts import views
urlpatterns = [
    path('admin/', admin.site.urls,),
    path('',include('adoption.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/<id>/',views.edit,name='edit_profile'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)