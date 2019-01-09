from django.conf.urls import  url
from django.urls import include, path
from . import views
from rest_framework import routers

app_name = "api"

# router  = routers.DefaultRouter()

# router.register('leadcapture', views.LeadViewSet)

urlpatterns = [
	
    path('leadcapture/', views.LeadViewSet.as_view()),
    

]