"""server_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from os import name
from django.contrib import admin
from django.urls import path
from unlock_keyring import views as unlock_views
from dashboard import views as dash_views
from usage_api import views as usage_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", unlock_views.unlock),
    path("monitoring/", dash_views.monitoring, name="Monitoring"),
    path("dash/", dash_views.dashboard, name="dashboard"),
    path("key/", dash_views.keys, name="keys"),
    path("add/", unlock_views.add_key, name="add_key"),
    path("usage/mem/", usage_views.memusage),
    path("usage/cpu/", usage_views.cpuusage),
    path("usage/test/", dash_views.test, name="usage_dashboard"),
    path("logout", dash_views.logout, name="logout"),
]
