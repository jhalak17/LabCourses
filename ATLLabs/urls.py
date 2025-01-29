from django.urls import path
from django.views.generic import TemplateView

from ATLLabs import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name = "homepage"),
    path('equipments/', views.equipment_list, name = "equipments"),
    path('equipments/<int:pk>/', views.equipment_detail, name = "equipment_detail"),
    path('equipments/enquiry', views.EquipmentEnquiry.as_view(), name = "equipment_enquiry"),
]