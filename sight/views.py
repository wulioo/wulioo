from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets

from common.paging import Pagination
from sight.models import Sight, Info, Ticket, Comment
from sight.serializers import SightSerializer, SightDetailSerializer, TicketSerializer, CommentSerializer


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


#
class SighDetailView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SightDetailSerializer

    def get_queryset(self):
        return Sight.objects.all()


class TicketListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TicketSerializer
    # lookup_field = 'sight_id'

    def get_queryset(self):
        sight = self.request.GET.get('sight_id', None)
        return Ticket.objects.filter(sight_id=sight)


class CommentListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CommentSerializer
    # lookup_field = 'sight_id'

    def get_queryset(self):
        sight = self.request.GET.get('sight_id', None)
        sight = Sight.objects.filter(pk=sight, is_valid=True).first()
        b = Comment.objects.filter(sight_id=sight)
        # c = b.images.filter(is_valid=True)
        # if sight:
        #     # return Comment.objects.filter(is_valid=True, sight=sight)
        #      return sight.comments.filter(is_valid=True)


        return Comment.objects.filter(sight_id=sight)