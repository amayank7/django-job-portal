from re import template
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Job, field_choices, field_choices_dict
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponseRedirect
from .forms import JobCreationForm
# Create your views here.

class index(View):
    def get(self, request):
        return render(request, "jobs/index.html", {'field_choices' : field_choices})
    
class listJobs(View):
    
    def get(self, request, *args, **kwargs):
        
        if kwargs['field'] not in field_choices_dict.keys():
            raise Http404('<h1>404</h1> <br><br><h3>The page cannot be found.</h3>')

        filtered_jobs = Job.objects.filter(field = kwargs['field']) 

        return render(request, "jobs/category_wise_list.html", {
            'field_choices' : field_choices,
            'field_chosen' : field_choices_dict[kwargs['field']],
            'joblist' : filtered_jobs
        })

class jobDetail(View):
    def get(self, request, *args, **kwargs):
        job = get_object_or_404(Job, pk = kwargs['id'])
        user = request.user
        type_user = None
        if user == job.recruiter:
            type_user = 'recruiter'
        elif job.applicants.filter(pk = user.pk).exists():
            type_user = 'applicant'
        else:    
            type_user = 'neither'
        return render(request, 'jobs/job_detail.html', {
            'job' : job,
            'type_user' : type_user,
            'field_choices' : field_choices
        })
class jobApply(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        job = get_object_or_404(Job, pk = kwargs['id'])
        if user.is_authenticated:
            if user != job.recruiter:
                job.applicants.add(user)
            type_user = None
            if user == job.recruiter:
                type_user = 'recruiter'
            elif job.applicants.filter(pk = user.pk).exists():
                type_user = 'applicant'
            else:    
                type_user = 'neither'
            
            return render(request, "jobs/apply.html", {
                'type_user' : type_user
            })
        else: 
            raise Http404

        
class createJob(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('users:login'))
        form = JobCreationForm()
        return render(request, 'jobs/create_job.html', {
            'form' : form
        })
    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('users:login'))
        form = JobCreationForm(request.POST)
        if not form.is_valid():
            return render(request, 'jobs/create_job.html', {
            'form' : form
            })
        new_job = form.save(commit = False)
        new_job.recruiter = request.user
        new_job.save()
        return HttpResponseRedirect(reverse_lazy('users:recruitment'))

class companyUpdate(View):
    def get(self, request):
        form = JobCreationForm()
        return render(request, 'jobs/company_update.html', {
            'form' : form
        })