# -*- coding: utf-8 -*-
from  django.conf.urls import url
from . import views


urlpatterns = [
        # 使用 pycharts 库 绘图，并在 Web 页面展示3D图形...
        url(r'^pychart3d/$', views.pyechart3d, name='pychart3d'),
        # 使用 echarts.js  渲染，并在 Web 页面展示折线图...
        url(r'^linechart/$', views.linechart, name='linechart'),
        # 使用 echarts.js 渲染，并在 Web 页面展示多维折线图...
        url(r'^multilinechart/$', views.multilinechart, name='multilinechart'),
        # 柱状图
        url(r'^barchart/$', views.barchart, name='barchart'),
        # 饼状图
        url(r'^piechart/$', views.piechart, name='piechart'),
        ]
