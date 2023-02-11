from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('customers/', views.CustomersView.as_view(), name="customers"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
