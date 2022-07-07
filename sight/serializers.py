# -*- coding:utf-8 -*-
# @Time : 2022/6/6 10:29
from rest_framework import serializers

from sight.models import Sight, Info, Ticket, Comment
from system.serializers import ImageRelatedSerializer


class SightSerializer(serializers.ModelSerializer):
    images = ImageRelatedSerializer(many=True)
    class Meta:
        model = Sight
        fields = "__all__"


class SightDetailSerializer(serializers.ModelSerializer):
    # sight = SightSerializer(many=False)

    class Meta:
        model = Sight
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    images = ImageRelatedSerializer(many=True)

    class Meta:
        model = Comment
        fields = "__all__"
