from django.conf.urls import include, url

urlpatterns = [
    url(r'^users/$', 'core.views.user_collection'),
    url(r'^users/(?P<pk>[0-9]+)$', 'core.views.user_element')
]
