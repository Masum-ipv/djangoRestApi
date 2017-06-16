from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from country import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^city/(?P<name>[\w-]+)/$', views.CityList.as_view()),
    url(r'^city/$', views.CityList.as_view()),
]