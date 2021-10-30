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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', unlock_views.home),
    path('monitoring/',unlock_views.data,name='Monitoring'),
    path('dash/',dash_views.home,name='dashboard'),
    path('key/',dash_views.keys,name='key'),
    path('add/',unlock_views.add,name='add')

]
