from django.db import models


# 设计和表对应的类，模型类
# Create your models here.

# 图书类

class BookInfo(models.Model):
    '''图书馆模型'''
    # 图书名称，ChairField说明是一个字符串，max_length指定字符串的最大长度
    btitle = models.CharField(max_length=20)
    # 出版日期，DateField说明是一个日期类型
    bpub_date = models.DateField()

# 实现数据库的一对多关系
class HeroInfo(models.Model):
    "人物模型"
    # 姓名
    hname = models.CharField(max_length=32)
    # 性别
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)
    # 生成人物和图书之间的一对多关系
    hbook = models.ForeignKey("BookInfo",on_delete=models.CASCADE)