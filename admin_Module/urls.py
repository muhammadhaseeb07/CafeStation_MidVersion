from django.urls import path
from . import views

app_name = 'admin_Module'
urlpatterns = [
    path('addInstitutes/', views.addInstitutes, name='addInstitutes'),
    path('notifications/', views.notifications, name='notifications'),
    path('approveRequest/', views.approveRequest, name='approveRequest'),
]