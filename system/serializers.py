# -*- coding:utf-8 -*-
# @Time : 2022/6/6 10:29
from rest_framework import serializers

from system.models import Slider


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"

