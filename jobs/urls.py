from django.urls import path 

urlpatterns = [
    path('jobs/', include('jobs.urls')),       

]
