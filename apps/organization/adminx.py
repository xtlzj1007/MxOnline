# -*- encoding:utf-8 -*-
__author__ = 'zuojie'
__date__ = '2017/2/25 21:27'

import xadmin
from .models import CityDict, CoureOrg, Teacher


# 城市
class CityDictAdmin(object):
    # 在admin中显示顺序
    list_display = ['name', 'desc', 'add_time']
    # 给admin添加搜索功能
    search_fields = ['name', 'desc']
    # 筛选字段
    list_filter = ['name', 'desc', 'add_time']


# 机构信息
class CoureOrgAdmin(object):
    """docstring for CoureOrg"""
    # 在admin中显示顺序
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
    # 给admin添加搜索功能
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    # 筛选字段
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']


# 教师信息
class TeacherAdmin(object):
    # admin中显示顺序
    list_display = ['org', 'name', 'work_years', 'work_compamy', 'work_position', 'pointa', 'click_nums', 'fav_nums',
                    'add_time']
    # 给admin添加搜索功能
    search_fields = ['org', 'name', 'work_years', 'work_compamy', 'work_position', 'pointa', 'click_nums', 'fav_nums']
    # 筛选字段
    list_filter = ['org', 'name', 'work_years', 'work_compamy', 'work_position', 'pointa', 'click_nums', 'fav_nums',
                   'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CoureOrg, CoureOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
