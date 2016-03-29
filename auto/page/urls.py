# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from page import views
from page.twviews import GoodListView, GoodDetailView

urlpatterns = patterns('',
    # url(r'^(?:(?P<cat_id>\d+)/)?$', views.index, name="index"),#урл дл категорий
    # url(r'^good/(?P<good_id>\d+)/$', views.good, name="good"),#урл для объекта
    url(r'^(?:(?P<cat_id>\d+)/)?$', GoodListView.as_view(),name = "index"),
    url(r'^good/(?P<good_id>\d+)/$', GoodDetailView.as_view(), name="good"),
)
