"""food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import food.views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^index',food.views.index,name='index_url'),
    
    url(r'^contact',food.views.contact,name='contact_url'),
    url(r'^blog',food.views.blog,name='blog_url'),
    url(r'^chef',food.views.chef,name='chef_url'),
    url(r'^menu',food.views.menu,name='menu_url'),
    url(r'^customerreg',food.views.customerreg,name='customerreg_url'),
    url(r'^login',food.views.login1,name='login_url'),
    url(r'^logout',food.views.logout1,name='logout_url'),
    url(r'^hotelreg',food.views.hotelreg,name='hotelreg_url'),
    url(r'^food',food.views.food,name='food_url'),
    url(r'^whotel',food.views.whotel,name='whotel_url'),
    url(r'^wcustomer',food.views.wcustomer,name='wcustomer_url'),
    url(r'^order',food.views.order,name='order_url'),
    url(r'^bill',food.views.bill,name='bill_url'),




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += url(r'^$',food.views.index),