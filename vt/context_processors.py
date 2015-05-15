from django.core.urlresolvers import resolve
from collections import OrderedDict


def navbar(request):
    menus = OrderedDict([
        ('api_doc', {'title': 'Documentation'}),
        ('user_collection_api', {'title': 'User collection'}),
    ])

    try:
        name = resolve(request.path).url_name
        if name in menus:
            menus[name]['active'] = True
    except:
        pass

    return {
        'menus': menus,
    }
