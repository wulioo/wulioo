"""travel_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework.routers import DefaultRouter

from sight.views import SightListView, SighDetailView, TicketListView, CommentListView

# router = DefaultRouter()
# # 景点列表
# router.register(r'sight/list', SightListView, basename='sight/list')
#
# router.register(r'sight/detail/<int:pk>/', SighDetailView, basename='sight/detail')
#
# urlpatterns = [
#
# ] + router.urls


urlpatterns = [
    # 2.2 景点详情
    path('sight/detail/<int:pk>', SighDetailView.as_view({'get': 'retrieve'})),
    # 2.1 景点列表接口
    path('sight/list', SightListView.as_view({'get': 'list'})),
    # 2.3 门票列表接口
    path('sight/ticket', TicketListView.as_view({'get': 'list'})),
    # 2.4 热门评论
    path('sight/comment', CommentListView.as_view({'get': 'list'})),

]
