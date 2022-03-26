from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('add', views.addCompanyView.as_view(), name = 'add-company')
]