from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (("男", "1"), ("女", "2"))


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True


class UserProfile(AbstractUser):
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=1, null=True, blank=True)
    mobile = models.CharField(max_length=11, verbose_name="手机号码", null=True, blank=True)
    image = models.ImageField(verbose_name="用户头像", upload_to="head_image/%Y/%m", default="default.jpg")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def unread_nums(self):
        # 未读消息数量
        return self.usermessage_set.filter(has_read=False).count()
