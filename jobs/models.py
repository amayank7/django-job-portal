from django.contrib.auth import get_user_model
from django.db import models
from companies.models import Company

# Create your models here.
field_choices = (('IT', 'Information Technology'), ('SL', 'Sales'), ('MG', 'Management'), ('AC', 'Analytics/Consulting'), ('OT', 'Other'))
field_choices_dict = dict(field_choices)

class Job(models.Model):
    job_title = models.CharField(max_length = 64)
    field = models.CharField(max_length = 2, choices = field_choices)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    description = models.TextField(null = True, blank = True)
    salary = models.IntegerField(null=True, blank = True)
    recruiter = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name = 'jobs_hiring')
    applicants = models.ManyToManyField(get_user_model(), related_name='jobs_applied', null=True, blank=True)

    def __str__(self):
        return f'{self.job_title} : {self.company.name}'


