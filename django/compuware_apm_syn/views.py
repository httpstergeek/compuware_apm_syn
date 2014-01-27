from django.contrib.auth.decorators import login_required
from splunkdj.decorators.render import render_to

# Imports for the setup view
from .forms import SetupForm
from django.core.urlresolvers import reverse
from splunkdj.setup import config_required
from splunkdj.setup import create_setup_view_context


@render_to('compuware_apm_syn:setup.html')
@login_required
def setup(request):
    return create_setup_view_context(
        request,
        SetupForm,
        reverse('gomez_networks:home'))


@render_to('compuware_apm_syn:home.html')
def home(request):
    return {
        "message": "Hello World from compuware_apm_syn!",
        "app_name": "compuware_apm_syn"
    }


@render_to('compuware_apm_syn:search.html')
@login_required
def search(request):
    return {
        "message": "Hello World from gomez_networks!",
        "app_name": "gomez_networks"
    }


@render_to('compuware_apm_syn:gomezoverview.html')
@login_required
def gomezoverview(request):
    return {
        "message": "Hello World from gomez_networks!",
        "app_name": "gomez_networks"
    }


@render_to('compuware_apm_syn:mid2site.html')
@login_required
def mid2site(request):
    return {
        "message": "Hello World from gomez_networks!",
        "app_name": "gomez_networks"
    }


@render_to('compuware_apm_syn:rtimeheat.html')
@login_required
def rtimeheat(request):
    return {
        "message": "Hello World from gomez_networks!",
        "app_name": "gomez_networks"
    }


@render_to('compuware_apm_syn:barline.html')
@login_required
def barline(request):
    return {
        "message": "Hello World from gomez_networks!",
        "app_name": "gomez_networks"
    }


@render_to('compuware_apm_syn:page2obj.html')
@login_required
def page2obj(request):
    return {
        "message": "Hello World from gomez_networks!",
        "app_name": "gomez_networks"
    }


@render_to('compuware_apm_syn:pageinfo.html')
@login_required
def pageinfo(request):
    return {
        "message": "Hello World from gomez_networks!",
        "app_name": "gomez_networks"
    }


@render_to('compuware_apm_syn:obj2host.html')
@login_required
def obj2host(request):
    return {
        "message": "Hello World from gomez_networks!",
        "app_name": "gomez_networks"
    }


@render_to('compuware_apm_syn:objinfo.html')
@login_required
def objinfo(request):
    return {
        "message": "Hello World from gomez_networks!",
        "app_name": "gomez_networks"
    }


@render_to('compuware_apm_syn:hostinfo.html')
@login_required
def hostinfo(request):
    return {
        "message": "Hello World from gomez_networks!",
        "app_name": "gomez_networks"
    }


@render_to('compuware_apm_syn:conninfo.html')
@login_required
def conninfo(request):
    return {
        "message": "Hello World from gomez_networks!",
        "app_name": "gomez_networks"
    }


@render_to('compuware_apm_syn:pageTimes.html')
@login_required
def pageTimes(request):
    return {
        "message": "Hello World from gomez_networks!",
        "app_name": "gomez_networks"
}
