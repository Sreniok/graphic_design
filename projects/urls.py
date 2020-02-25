from django.conf.urls import url, include
from .views import all_projects


urlpatterns = [
    url(r'^$', all_projects, name='projects'),
]