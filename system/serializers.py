# -*- coding:utf-8 -*-
# @Time : 2022/6/6 10:29
from rest_framework import serializers

from system.models import Slider, ImageRelated


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class ImageRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRelated
        fields = "__all__"
