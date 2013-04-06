from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import list_detail, create_update 

from django.conf import settings
from dclog.views import *
from dclog.models import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

log_list = {
    # 'queryset': Log.objects.all(),
    'queryset': Log.objects.order_by('-eventTime'),
    'template_name': 'display_logs.html',
}

urlpatterns = patterns('',
    # Example:
    # (r'^nhdc/', include('nhdc.foo.urls')),
	
	# Datacenter log urls
    url(r'^$', 'django.views.generic.list_detail.object_list', {'queryset': Log.objects.order_by('-eventTime'),'template_name': 'display_logs.html'}, name='log_list'),
    url(r'^log/(?P<object_id>\d+)/', 'django.views.generic.list_detail.object_detail', {'queryset': Log.objects.order_by('-eventTime'),'template_name': 'display_log.html'}, name='log-display'),
	url(r'^edit/log/(?P<log_id>\d+)/', login_required(editLog), name='log-edit'),
    url(r'^log/create/', login_required(newLog), name='newLog'),

	# the login form
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'auth.html'}, name='login'), # https://docs.djangoproject.com/en/dev/topics/auth/
	
    # protected urls that will require login
	url(r'^alarm/create/', login_required(newAlarm), name='newAlarm'),
    url(r'^area/create/', login_required(newArea), name='newArea'),
    url(r'^update/(?P<log_id>\d+)/create/', login_required(newUpdate), name='newUpdate'),
    url(r'^facility_type/create/', login_required(newFacilityType), name='newFacilityType'),
	
    url(r'^search/', login_required(search), name='search'),
	
	# Static media 
    url(r'^appmedia/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT,'show_indexes': True }),
    
    # https://docs.djangoproject.com/en/dev/topics/auth/#django.contrib.auth.views.logout_then_login
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'), #https://docs.djangoproject.com/en/dev/topics/auth/#module-django.contrib.auth.views

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)