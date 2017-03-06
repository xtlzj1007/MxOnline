# -*- encoding:utf-8 -*-
__author__ = 'zuojie'
__date__ = '2017/2/25 21:27'

import xadmin
from .models import UserAsk, CourseComments, UserCourse, UserMessage, UserFavorite


class UserAskAdmin(object):
    # 在admin中显示顺序
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    # 给admin添加搜索功能
    search_fields = ['name', 'mobile', 'course_name']
    # 筛选字段
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


# 课程评论
class CourseCommentsAdmin(object):
    # 在admin中显示顺序
    list_display = ['user', 'course', 'comments', 'add_time']
    # 给admin添加搜索功能
    search_fields = ['user', 'course', 'comments']
    # 筛选字段
    list_filter = ['user__username', 'course__name', 'comments', 'add_time']


# 用户收藏
class UserFavoriteAdmin(object):
    # 在admin中显示顺序
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    # 给admin添加搜索功能
    search_fields = ['user', 'fav_id', 'fav_type', ]
    # 筛选字段
    list_filter = ['user__username', 'fav_id', 'fav_type', 'add_time']


# 用户消息
class UserMessageAdmin(object):
    # 在admin中显示顺序
    list_display = ['user', 'message', 'has_read', 'add_time']
    # 给admin添加搜索功能
    search_fields = ['user', 'message', 'has_read']
    # 筛选字段
    list_filter = ['user', 'message', 'has_read', 'add_time']


# 用户学习的课程
class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
