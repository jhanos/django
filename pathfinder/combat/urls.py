from django.conf.urls import patterns, include, url

urlpatterns = patterns('combat.views',
    # Examples:
    # url(r'^$', 'pathfinder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'home', name='home'),
    url(r'^acceuil$', 'home', name='home'),
    url(r'^create/creature/(?P<name>\w+)/$', 'createCreature',name='createCreature'),
    #url(r'^create/weapon/$', 'createWeapon',name='createWeapon'),
    url(r'^create/(?P<type>\w+)/$', 'create',name='create'),
    url(r'^fight/(?P<id>\w+)/$', 'fight'),
    url(r'^display','display',name='display'),
    url(r'^create/success','success'),
)
