from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets

from system.models import Slider
from system.serializers import SliderSerializer


class SliderList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Slider.objects.filter(is_valid=True)
    serializer_class = SliderSerializer

