# Generated by Django 4.0.1 on 2022-03-18 12:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='YearsOfExperience',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(15), django.core.validators.MaxValueValidator(110)]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('[0-9]{10}')]),
        ),
    ]
