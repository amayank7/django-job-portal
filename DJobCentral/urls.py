"""DJobCentral URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('users/', include('users.urls')),
    path('jobs/', include('jobs.urls')),
    path('companies/', include('companies.urls')),
    path('search/<str:category>/', views.searchSpecificResults.as_view(), name = 'search-specific'),
    path('search/', views.searchResults.as_view(), name = 'search'),
    path('', views.homepage.as_view(), name = 'homepage'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
]
