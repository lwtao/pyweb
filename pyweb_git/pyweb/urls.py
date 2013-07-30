from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import views
urlpatterns = patterns('',
                       ('^hello/$',views.hello),
                       (r'^addhours/(\d)/$',views.add_hours),
                       ('^ttest/$',views.t_test),
                       ('^zdx_test/$',views.zdx_test),
                       ('^show_xoljua/$',views.show),
                       ('^modify_swqgerz/$',views.modify),
                       ('^jump/$',views.jump),
                       ('^jump_tongji/(.*)/$',views.jump_tongji),
                       ('^index/$',views.index)
    # Examples:
    # url(r'^$', 'pyweb.views.home', name='home'),
    # url(r'^pyweb/', include('pyweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
