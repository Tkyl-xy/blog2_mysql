from django.db import models

# Create your models here.
class Display(models.Model):
    class Meta:
        db_table = 'own'

    id = models.AutoField(primary_key=True)
    description = models.CharField(default="在这里写作品的简介", max_length=100)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(default="作品标题", max_length=50)

    #这里是实现管理标题，便于管理以后的描述标题
    def __str__(self):
        return self.title
