# coding: utf-8
from django.db import models
from django.contrib import admin
# Create your models here.
class Queue(models.Model):
    secret_number     = models.IntegerField('密码单号',unique=True)  # 密码单号,字段唯一
    car_number        = models.CharField('车号', max_length=20)  #
    queue_number      = models.IntegerField('排队号码')  #
    phone_number      = models.CharField('手机号码', max_length=20)  # 若要展示要做*号处理
    driver_name       = models.CharField('司机姓名', max_length=20)  # 司机姓名
    items             = models.CharField('物品种类', max_length=20)  # 物品种类
    in_time           = models.DateTimeField('进厂时间',auto_now_add=True) # 进厂时间
    out_time          = models.DateTimeField('离厂时间',auto_now=True ) #出厂时间
    status            = models.BooleanField('离厂',default=False)               #车辆状态,是否出厂,默认未出厂

    class Meta:
        verbose_name = '排队信息维护'
        verbose_name_plural = '排队信息维护'
        ordering = ['-out_time']

    def __str__(self):              # __unicode__ on Python 2
        return "%s " % self.secret_number

class QueueAdmin(admin.ModelAdmin):
    list_display      = ('car_number','queue_number','secret_number','in_time','out_time','status',)
    search_fields     = ('secret_number',)
    list_max_show_all = 50

class Result(models.Model):
    queue = models.OneToOneField(
        Queue,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    water_content                = models.FloatField('水分含量',max_length=10,null=True,blank=True) # 水分含量
    impurity                     = models.FloatField('杂质含量',max_length=10,null=True,blank=True) # 杂质含量
    whole_rice_rate              = models.FloatField('整米率',max_length=10,null=True,blank=True)   # 整米率
    lesion                       = models.FloatField('病斑',max_length=10,null=True,blank=True)     # 病斑
    chalkiness                   = models.FloatField('垩白',max_length=10,null=True,blank=True)     # 垩白
    out_of_rice_rate             = models.FloatField('出米率',max_length=10,null=True,blank=True)   # 出米率
    mixed                        = models.FloatField('互混',max_length=10,null=True,blank=True)             # 互混
    yellow_grain_rice            = models.FloatField('黄粒米',max_length=10,null=True,blank=True)           # 黄粒米
    inspection_creat_time        = models.DateTimeField('创建时间',auto_now_add=True,blank=True)           # 创建时间
    is_good                      = models.BooleanField('合格',default=True)               #是否合格,默认合格

    class Meta:

        verbose_name        = '化验信息维护'
        verbose_name_plural = '化验信息维护'


    def __str__(self):              # __unicode__ on Python 2
        return "%s " % self.queue.secret_number

class ResultAdmin(admin.ModelAdmin):
    list_display = ('queue','inspection_creat_time', 'is_good')
    search_fields = ('queue',)
    list_max_show_all = 50

