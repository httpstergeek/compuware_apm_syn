from django.conf.urls import patterns, include, url
from splunkdj.utility.views import render_template as render

urlpatterns = patterns('',
    url(r'^home/$', 'compuware_apm_syn.views.home', name='home'),
    url(r'^setup/$', 'compuware_apm_syn.views.setup', name='setup'),
    url(r'^search/$', 'compuware_apm_syn.views.search', name='search'),
    url(r'^gomezoverview/$', 'compuware_apm_syn.views.gomezoverview', name='gomezoverview'),
    url(r'^mid2site/$', 'compuware_apm_syn.views.mid2site', name='mid2site'),
    url(r'^rtimeheat/$', 'compuware_apm_syn.views.rtimeheat', name='rtimeheat'),
    url(r'^barline/$', 'compuware_apm_syn.views.barline', name='barline'),
    url(r'^page2obj/$', 'compuware_apm_syn.views.page2obj', name='page2obj'),
    url(r'^pageinfo/$', 'compuware_apm_syn.views.pageinfo', name='pageinfo'),
    url(r'^obj2host/$', 'compuware_apm_syn.views.obj2host', name='obj2host'),
    url(r'^objinfo/$', 'compuware_apm_syn.views.objinfo', name='objinfo'),
    url(r'^hostinfo/$', 'compuware_apm_syn.views.hostinfo', name='hostinfo'),
    url(r'^conninfo/$', 'compuware_apm_syn.views.conninfo', name='conninfo'),
    url(r'^pageTimes/$', 'compuware_apm_syn.views.pageTimes', name='pageTimes'),
        
)
