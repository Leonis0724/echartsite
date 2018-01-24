# -*- coding: utf-8 -*-

from django.db import models


class PageViewStatistics(models.Model):
    ''' 广告页面访问量统计 '''

    # 时间选择
    WEEK_CHOICES = (
            ('1', '周一'),
            ('2', '周二'),
            ('3', '周三'),
            ('4', '周四'),
            ('5', '周五'),
            ('6', '周六'),
            ('7', '周日'),
            )

    # 访问方式
    PV_WAY = (
            ('邮件营销', '邮件营销'),
            ('联盟广告', '联盟广告'),
            ('视频广告', '视频广告'),
            ('直接访问', '直接访问'),
            ('搜索引擎', '搜索引擎'),
            )



    # 星期
    time_week = models.CharField(max_length=100, choices=WEEK_CHOICES, null=False)
    # 访问方式
    view_way = models.CharField(max_length=256, choices=PV_WAY)

    # 访问量
    page_views = models.IntegerField()

    # 统计日期
    pub_date = models.DateField()

    class Meta:
        db_table = 'pv_statistics'

