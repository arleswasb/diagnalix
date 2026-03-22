from django.urls import path
from .views import MedicalCardList

urlpatterns = [
    path('cards/', MedicalCardList.as_view(), name='medicalcard-list'),
]
