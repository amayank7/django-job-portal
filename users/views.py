from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.views import View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, UserEditForm
from .models import CustomUser
from jobs.models import Job
# Create your views here.

class CustomRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

class UserIndex(View):
    def get(self, request):
        return render(request, 'users/index.html', {
        })

class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        visiting_profile = get_object_or_404(CustomUser, username = kwargs['id'])
        
        return render(request, 'users/profile-detail.html', {
            'profile' : visiting_profile
        } )

class EditProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('users:login'))
        form = UserEditForm(instance=request.user)
        return render(request, 'users/edit-profile.html', {
            'form' : form
        })
    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('users:login'))
        form = UserEditForm(request.POST, instance=request.user)
        if not form.is_valid():
            return render(request, 'users/edit-profile.html', {
            'form' : form
            })
        form.save()
        return HttpResponseRedirect(reverse_lazy('users:profile', args=[request.user.username]))

class AppliedJobsView(View):
    def get(self, request):
        return render(request, 'users/jobs-applied.html')

class DeleteApplication(View):
    def post(self, request):
        if not request.user.is_authenticated:
            raise Http404
        request.user.jobs_applied.remove(Job.objects.get(pk=request.POST['job_id']))
        return render(request, 'users/jobs-applied-htmx.html')

class RecruiterView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('users:login'))
        return render(request, 'users/jobs-hiring.html')

class deleteApplicant(View):
    def post(self, request):
        job = Job.objects.get(pk = request.POST['job_id'])
        users = get_user_model()
        job.applicants.remove(users.objects.get(username = request.POST['applicant']))
        return render(request, 'users/delete-applicant.html', {
            'job': job
        })

class deleteJob(View):
    def post(self, request):
        Job.objects.get(pk = request.POST['job_id']).delete()
        return render(request, 'users/blank.html')

        