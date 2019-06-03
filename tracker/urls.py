"""tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from tracker_app import urls as trackerapp_url
from cart import urls as cart_urls
from tracker_app.views import home, add_bug, edit_bug,delete_bug, feature, add_feature, edit_feature
from django.conf import settings
from django.conf.urls.static import static 
from django.shortcuts import HttpResponse
from checkout import urls as checkout_url
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include(trackerapp_url.urlpatterns)),
    url(r'^$', home, name="home"),
    url(r'add/$', add_bug,name="add_bug"),
    url(r'edit/(?P<id>\d+)$', edit_bug),
    url(r'delete/(?P<id>\d+)$', delete_bug,name="delete_bug"),
    url(r'add_feature/$', add_feature,name="add_feature"),
    url(r'edit_feature/(?P<id>\d+)$', edit_feature, name="edit_feature"),
    url(r'^feature/', feature, name="feature"),
    url(r'^cart/', include(cart_urls.urlpatterns)),
    url(r'^checkout/', include(checkout_url.urlpatterns))
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)