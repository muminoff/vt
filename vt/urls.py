from django.conf.urls import include, url
from django.conf import settings

urlpatterns = [
    url(r'^$', 'core.views.api_doc'),
    url(r'^users/$', 'core.views.user_collection'),
    url(r'^users/(?P<pk>[0-9]+)$', 'core.views.user_element')
]

if settings.DEBUG:
    urlpatterns = urlpatterns + [
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve'),
]
