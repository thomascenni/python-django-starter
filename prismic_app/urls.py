from django.urls import reverse, path, re_path, include
from prismic_app import views


urlpatterns = [
    path(
        route='',
        view=views.index,
        name='index'
    ),
    re_path(
        route=r'^document/(?P<id>[-_a-zA-Z0-9]{16})/(?P<slug>.*)',
        view=views.detail,
        name='document'
    ),
    path(
        route='preview/',
        view=views.preview,
        name='preview'
    ),
]
