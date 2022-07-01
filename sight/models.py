from django.db import models
# from ckeditor.fields import RichTextField
from system.models import ImageRelated

from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.
from common.models import CommonModel


class Sight(CommonModel):
    """ 景点基础信息 """

    name = models.CharField('名称', max_length=64)
    desc = models.CharField('描述', max_length=256)
    main_img = models.ImageField('主图', upload_to='%Y%m/sight/', max_length=256)
    banner_img = models.ImageField('详情主图', upload_to='%Y%m/sight/', max_length=256)
    content = models.TextField('详细')
    # content = RichTextField('详细')
    score = models.FloatField('评分', default=5)
    min_price = models.FloatField('最低价格', default=0)
    province = models.CharField('省份', max_length=32)
    city = models.CharField('市区', max_length=32)
    area = models.CharField('区/县', max_length=32, null=True)
    town = models.CharField('乡镇', max_length=32, null=True)

    is_top = models.BooleanField('是否为精选景点', default=False)
    is_hot = models.BooleanField('是否为热门景点', default=False)

    images = GenericRelation(ImageRelated,
                             verbose_name='关联的图片',
                             related_query_name='rel_sight_iamges')

    class Meta:
        db_table = 'sight'
        ordering = ['-updated_at']
        verbose_name = '景点基础信息'
        verbose_name_plural = '景点基础信息'

    def __str__(self):
        return self.name

    @property
    def image_count(self):
        """ 景点图片的数量 """
        return self.images.filter(is_valid=True).count()


#
# class Info(models.Model):
#     """ 景点详情 """
#     sight = models.OneToOneField(Sight, on_delete=models.CASCADE, verbose_name='关联景点')
#     entry_explain = RichTextField('入园参考', max_length=1024, null=True, blank=True)
#     play_way = RichTextField('特色玩法', null=True, blank=True)
#     tips = RichTextField('温馨提示', null=True, blank=True)
#     traffic = RichTextField('交通到达', null=True, blank=True)
#
#     class Meta:
#         db_table = 'sight_info'
#         verbose_name = '景点详情'
#         verbose_name_plural = '景点详情'
