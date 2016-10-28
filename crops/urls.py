# -*- coding: utf-8 -*-
#
# author: william tiria wamburu | tiriawamburu@gmail.com
#

from crops import views

from django.conf.urls import url

urlpatterns = [
    url(r'^index/$', views.index, name="index"),

    url(r'^crops/$', views.crops, name="crops"),

    url(r'^crops/table/$', views.crops_table, name="crops-table"),

    url(r'^minerals/$', views.minerals, name="minerals"),

    url(r'^regions/$', views.regions, name="regions"),

    url(r'^analysis/crop-select/$', views.crop_select, name="crop-select"),

    url(r'^analysis/region-select/(?P<crop_pk>[0-9]+)/$', views.region_select, name="region-select"),

    url(r'^analysis/land-size-select/(?P<crop_pk>[0-9]+)/(?P<region_pk>[0-9]+)/$', views.land_size_select, name="land-size-select"),

    url(r'^analysis/working/(?P<crop_pk>[0-9]+)/(?P<region_pk>[0-9]+)/(?P<land_size>[0-9]+)/$', views.working, name="working"),

    url(r'^analysis/results/(?P<crop_pk>[0-9]+)/(?P<region_pk>[0-9]+)/(?P<land_size>[0-9]+)/$', views.results, name="results"),

    url(r'^add-crop/$', views.add_crop, name="add-crop"),

    url(r'^add-region/$', views.add_region, name="add-region"),

    url(r'^add-mineral/$', views.add_mineral, name="add-mineral"),

    url(r'^add-region-mineral/$', views.add_region_mineral, name="add-region-mineral"),

    url(r'^add-crop-mineral/$', views.add_crop_mineral, name="add-crop-mineral"),
]
