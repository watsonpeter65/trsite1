from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testy', views.testy, name='testy'),    
    path('training_listing', views.training_listing, name='training_listing'),            
    path('jobs_browse', views.jobs_browse, name='jobs_browse'),     
   # path('courseenquire', views.courseenquire, name='courseenquire'),     
    path('courseenquire/<str:section_id>/', views.courseenquire, name='courseenquire'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)