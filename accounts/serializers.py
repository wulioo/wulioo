# -*- coding:utf-8 -*-
# @Time : 2022/6/6 10:29
from rest_framework import serializers

from accounts.models import User
from sight.models import Sight, Info, Ticket, Comment
from system.serializers import ImageRelatedSerializer


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


     #序列化器中验证参数
    def validate_password(self, value):
        if(value != self.context['request'].data.get('checkpassword')):
            raise serializers.ValidationError('密码不一致')

        return value

    def validate_username(self, value):
        print(value)
        return value