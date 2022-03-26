from django.shortcuts import render
from django.views import View
from jobs.models import Job
from companies.models import Company
from django.contrib.auth import get_user_model
from django.db.models import Q

class homepage(View):
    def get(self, request):
        return render(request, 'homepage.html')

class searchResults(View):
    def get(self, request):
        query = request.GET['search']
        results = {}
        um = get_user_model()

        return render(request, 'search-results.html', {
            'query' : query,
            'results' : results
        })

class searchSpecificResults(View):
    def get(self, request, *args, **kwargs):
        query = request.GET['search']
        if kwargs['category'] == 'all':
            results = {}
            um = get_user_model()
            results['jobs'] = Job.objects.filter(job_title__contains = query)
            results['users'] = um.objects.filter(Q(first_name__contains = query) | Q(last_name__contains = query) | Q(username__contains = query) | Q(email = query) | Q(phone = query))
            results['companies'] = Company.objects.filter(name__contains = query)
            count = results['jobs'].count() + results['users'].count() + results['companies'].count()
        
        elif kwargs['category'] == 'jobs':
            results = Job.objects.filter(job_title__contains = query)
            count = results.count()
        
        elif kwargs['category'] == 'users':
            um = get_user_model()
            results = um.objects.filter(Q(first_name__contains = query) | Q(last_name__contains = query) | Q(username__contains = query) | Q(email = query) | Q(phone = query))
            count = results.count()
        
        elif kwargs['category'] == 'companies':
            results = Company.objects.filter(name__contains = query)
            count = results.count()
        
        return render(request, 'search-spec-results.html', {
            'category' : kwargs['category'],
            'query' : query,
            'results' : results,
            'count' : count
        })

