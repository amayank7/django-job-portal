from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.index.as_view(), name = 'job-index'), 
    path('create', views.createJob.as_view(), name = 'create-job'),
    path('create/company_reload', views.companyUpdate.as_view(), name = 'company-update'),
    path('detail/<str:id>', views.jobDetail.as_view(), name = 'job-detail'),
    path('detail/<str:id>/apply', views.jobApply.as_view(), name = 'job-apply'),
    path('<str:field>', views.listJobs.as_view(), name = 'job-list'),
]