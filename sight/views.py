from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets

from common.paging import Pagination
from sight.models import Sight
from sight.serializers import SightSerializer


class SightListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SightSerializer
    pagination_class = Pagination

    def get_queryset(self):
        query = Q(is_valid=True)
        # 1. 热门景点
        is_hot = self.request.GET.get('is_hot', None)
        if is_hot:
            query = query & Q(is_hot=True)

        # 2. 精选景点
        is_top = self.request.GET.get('is_top', None)
        if is_top:
            query = query & Q(is_top=True)

        # 3. 景点名称搜索
        name = self.request.GET.get('name', None)
        if name:
            query = query & Q(name__icontains=name)

        queryset = Sight.objects.filter(query)
        return queryset
