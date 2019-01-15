from django.db import models

# Create your models here.
class Display(models.Model):

    class Meta:
        #这个是创建数据库表
        db_table = 'own'
        #这个是给模型类起一个更可读的名字
        verbose_name_plural = '作品展集'

    id = models.AutoField(primary_key=True)
    description = models.CharField(default="在这里写作品的简介", max_length=100, verbose_name='作品简介')
    image = models.ImageField(upload_to='images/', verbose_name='图片名称')
    title = models.CharField(default="作品标题", max_length=50, verbose_name='作品标题')

    #这里是实现管理标题，便于管理以后的描述标题
    def __str__(self):
        return self.title
