from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pathfinder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'combat.views.home', name='home'),
    #url(r'^admin/', include('admin.site.urls')),
    url(r'^combat/', include('combat.urls')),
)
