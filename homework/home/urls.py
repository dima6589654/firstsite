"""
URL configuration for homework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path

from home.views import PersonFormView, ChildFormView, IceCreamFormView, IceCreamKioskFormView

urlpatterns = [
    path('person/', PersonFormView.as_view(), name='person'),
    path('child/', ChildFormView.as_view(), name='child'),
    path('icecream/', IceCreamFormView.as_view(), name='icecream'),
    path('', IceCreamKioskFormView.as_view(), name='kiosk'),
]
