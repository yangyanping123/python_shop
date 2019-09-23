from django.db import models

# Create your models here.
class UserMessage(models.Model):
    name=models.CharField(max_length=20,verbose_name=u"用户名") #指定必须长度
    email=models.EmailField(verbose_name=u"邮箱")
    address=models.CharField(max_length=100,verbose_name=u"地址")
    message=models.TextField(verbose_name=u"消息")
    class Meta:
         verbose_name=u"用户留言信息"
        #verbose_name_plural=u"用户留言详情表"#附属信息
        #db_table="user_massage" #默认表明
       # ordering="-id" #order


