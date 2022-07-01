# -*- coding:utf-8 -*-
# @Time : 2022/7/1 15:47
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework.response import Response


class Pagination(PageNumberPagination):
    page_size = 2
    # page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100

    # 重写分页渲染结果
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('per_page', self.page.paginator.per_page),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),

        ]))
