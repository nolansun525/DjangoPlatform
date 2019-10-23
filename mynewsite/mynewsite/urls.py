"""mynewsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from mysite.views import about, listing, disp_detail, index
from django.conf.urls import url
from mysite import views, view2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('list/', listing),
    path('list/<str:sku>/', disp_detail),
    # path('', index),
    path('ajax_add/', views.ajax_add),
    path('findresult/', views.findresult),
    path('', view2.coverage),
    path('coverageSearch/', view2.coverageSearch, name='coverageSearch'),

]

