from django.urls import reverse, path, re_path, include
from prismic_app import views


urlpatterns = [
    path(
        route='',
        view=views.index,
        name='index'
    ),
    path(
        route='post/<slug:uid>',
        view=views.detail,
        name='document'
    ),
    path(
        route='preview/',
        view=views.preview,
        name='preview'
    ),
]
