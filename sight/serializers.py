# -*- coding:utf-8 -*-
# @Time : 2022/6/6 10:29
from rest_framework import serializers

from sight.models import Sight


class SightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sight
        fields = "__all__"

