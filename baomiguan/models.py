from django.db import models

# Create your models here.
#答案表 
class anwserTable(models.Model):
    question = models.CharField(max_length=200)     #问题字段
    imgpath=  models.CharField(max_length=20)      #答案字段
    def __str__(self):
        return self.question