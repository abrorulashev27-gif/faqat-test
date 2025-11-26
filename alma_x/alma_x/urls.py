"""
URL configuration for alma_x project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from shop.views import PhoneListApiView, PhoneCreateApiView, PhoneEditApiView, PhoneDeleteApiView, PhoneDetailApiView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('phones/', PhoneListApiView.as_view(), name='phones'),
    path('phones/create/', PhoneCreateApiView.as_view(), name='phone_create'),
    path('phones/edit/<int:pk>/', PhoneEditApiView.as_view(), name='edit'),
    path('phones/delete/<int:pk>/', PhoneDeleteApiView.as_view(), name='phone-delete'),
    path('phones/detail/<int:pk>/', PhoneDetailApiView.as_view(), name='phone-detail'),

]
