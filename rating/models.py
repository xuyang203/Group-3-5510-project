from django.db import models

class Rating(models.Model):
    
    Ltd = models.FloatField('Ltd',default='')
    EBITDA = models.FloatField('EBITDA',default='')
    Cag = models.FloatField('Cag',default='')
    Pol = models.FloatField('Pol',default='')
    Roe = models.FloatField('Roe',default='')
    Se = models.FloatField('Se',default='')
    OP = models.FloatField('OP',default='')
    It = models.FloatField('It',default='')
    Cat = models.FloatField('Cat',default='')
    Ncf  = models.FloatField('Ncf',default='')
    Ibd = models.FloatField('Ibd',default='')
    Alr = models.FloatField('Alr',default='')
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now=True)
    result = models.TextField('result',default='')
    username = models.TextField('username',default='')

    def _str_(self):
        return 'username %s'%(self.username)
# Create your models here.
