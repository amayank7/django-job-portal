from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AddCompanyForm
from .models import Company
from django.db.utils import IntegrityError
# Create your views here.

class addCompanyView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("users:login"))
        form = AddCompanyForm()
        return render(request, "companies/add-company.html", {
            'form': form
        })
    def post(self, request):
            form = AddCompanyForm(request.POST)
            if form.is_valid():
                try:
                    new_comp = form.save(commit = False)
                    new_comp.name_lower = form.cleaned_data['name'].lower().strip()
                    if form.is_valid():
                        new_comp = form.save()
                except IntegrityError:
                    return render(request, "companies/blank.html", {
                        'msg': "The company already exists in the database."
                    })
                
                return render(request, "companies/blank.html", {
                    'msg' : 'Done!'
                })
            else:
                return render(request, "companies/add-company.html", {
                'form': form
            })
