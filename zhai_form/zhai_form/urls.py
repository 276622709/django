from django.conf.urls import patterns, include, url
#from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zhai_form.views.home', name='home'),
    # url(r'^zhai_form/', include('zhai_form.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
      url(r'^$', 'tools.views.index', name='home'),
      url(r'^index/', 'tools.views.index', name='ip'),
      url(r'^command/', 'tools.views.command', name='ip1'),
      url(r'^command1/', 'tools.views.command1', name='ip11'),
)
