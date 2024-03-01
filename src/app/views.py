from django.shortcuts import render

# Create your views here.
from .functions import (
    get_banner,
    get_some_vendor,
    get_some_location,
    get_about,
    get_why_choose,
    get_config,
)


def home(request):

    get_banners = get_banner({'publish':True})
    get_some_vendors = get_some_vendor({'publish':True,'location_or_vendor': 'vente'})
    get_some_locations = get_some_location({'publish':True,'location_or_vendor': 'location'})
    get_abouts = get_about({'publish':True})
    get_why_chooses = get_why_choose({'publish':True})
    get_configs = get_config({'publish':True})

    template_name = "layout/index.html"
    context = {
        'get_banners': get_banners,
        'get_some_vendors': get_some_vendors,
        'get_some_locations': get_some_locations,
        'get_abouts': get_abouts,
        'get_why_chooses': get_why_chooses,
        'get_configs': get_configs
    }
    return render(request, template_name, context)