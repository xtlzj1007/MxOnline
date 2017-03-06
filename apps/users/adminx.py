# -*- encoding:utf-8 -*-
__author__ = 'zuojie'
__date__ = '2017/2/25 19:57'

import xadmin

from .models import EmailVerifyRecord
from .models import Banner
from  xadmin import views


class BaseSetting(object):
    """xadmin全局设置"""
    # 使用xadmin主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 修改xadmin标题
    site_title = "ZJ后台管理系统"
    # 修改xadmin底部信息
    site_footer = "ZJ在线网"
    # 折叠测边栏
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    # 在admin中显示顺序
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 给admin添加搜索功能
    search_fields = ['code', 'email', 'send_type']
    # 筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BanerAdmin(object):
    # 在admin中显示顺序
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 给admin添加搜索功能
    search_fields = ['title', 'image', 'url', 'index']
    # 筛选字段
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BanerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
