from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from diagnosis import views

app_name = 'diagnosis'
urlpatterns = [
    path('dental/', views.DiagnosisSummaryDentalView.as_view(),
         name='dental-diagnosis'),
    path('dental/<int:id>/', views.DiagnosisSummaryDentalDetailView.as_view(),
         name='dental-diagnosis-detail'),
    path('teeth/', views.DiagnosisSummaryTeethView.as_view(), name='teeth-diagnosis'),
    path('teeth/<int:id>/', views.DiagnosisSummaryTeethDetailView.as_view(),
         name='teeth-diagnosis-detail'),
    path('caries/', views.DiagnosisSummaryCariesView.as_view(),
         name='caries-diagnosis'),
    path('caries/<int:id>/', views.DiagnosisSummaryCariesDetailView.as_view(),
         name='caries-diagnosis-detail'),
]
