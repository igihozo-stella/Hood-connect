from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views


urlpatterns = [
    url(r'^admin/', admin.site.urls,name=admin),
    url(r'',include('neighbours.urls')),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    # url(r'^logout/$', views.logout, {"next_page": '/'}), 
]
