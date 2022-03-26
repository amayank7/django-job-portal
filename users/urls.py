from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.UserIndex.as_view(), name = 'user-index'),
    path('register', views.CustomRegistrationView.as_view(), name = 'register'),
    path('profiles/<str:id>', views.UserProfileView.as_view(), name = 'profile'),
    path('applications', views.AppliedJobsView.as_view(), name = 'applications'),
    path('applications/delete', views.DeleteApplication.as_view(), name = 'delete_application'),
    path('edit-profile', views.EditProfileView.as_view(), name = 'edit-profile'),
    path('recruitment', views.RecruiterView.as_view(), name = 'recruitment'),
    path('delete-applicant', views.deleteApplicant.as_view(), name = 'delete_applicant'),
    path('delete-job', views.deleteJob.as_view(), name = 'delete_job'),
    path('', include('django.contrib.auth.urls'))
]