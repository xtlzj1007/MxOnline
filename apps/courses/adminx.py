# -*- encoding:utf-8 -*-
__author__ = 'zuojie'
__date__ = '2017/2/25 20:42'

import xadmin

from .models import Course, CourseResource, Video, Lesson


class CourseAdmin(object):
    # 在admin中显示顺序
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time']
    # 给admin添加搜索功能
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums']
    # 筛选字段
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']


class CourseResourceAdmin(object):
    # 在admin中显示顺序
    list_display = ['course', 'name', 'download', 'add_time']
    # 给admin添加搜索功能
    search_fields = ['course', 'name', 'download']
    # 筛选字段
    list_filter = ['course__name', 'name', 'download', 'add_time']


class VideoAdmin(object):
    # 在admin中显示顺序
    list_display = ['lesson', 'name', 'add_time']
    # 给admin添加搜索功能
    search_fields = ['lesson', 'name']
    # 筛选字段
    list_filter = ['lesson__name', 'name', 'add_time']


class LessonAdmin(object):
    # 在admin中显示顺序
    list_display = ['course', 'name', 'add_time']
    # 给admin添加搜索功能
    search_fields = ['course', 'name']
    # 筛选字段
    list_filter = ['course__name', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
