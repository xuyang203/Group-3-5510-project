from django.db import models



class Cop(models.Model):
    copname = models.CharField('公司名称',max_length=30,unique=True)
    copinfo = models.TextField('公司简介',default='')
    #create_time = models.DateTimeField('创建时间',auto_now_add=True)
    #update_time = models.DateTimeField('更新时间',auto_now=True)
    creditlevel = models.TextField('信用水平',default='')
    industry = models.TextField('行业',default='')
    solvency = models.TextField('solvency',default='')
    profitmargin = models.TextField('profitmargin',default='')
    incomegrowth = models.TextField('incomegrowth',default='')
    profitgrowth = models.TextField('profitgrowth',default='')
    cashdebt = models.TextField('cashdebt',default='')
    cashflowdebt = models.TextField('cashflowdebt',default='')
    turnoverrate = models.TextField('turnoverrate',default='')
    debtratio = models.TextField('debtratio',default='')
    roegrowth = models.TextField('roegrowth',default='')
    
    def _str_(self):
        return 'copname %s'%(self.copname)
        
class Data(models.Model):
    industry = models.TextField('行业',default='')
    solvency = models.FloatField('solvency',default='')
    profitmargin = models.FloatField('profitmargin',default='')
    incomegrowth = models.FloatField('incomegrowth',default='')
    profitgrowth = models.FloatField('profitgrowth',default='')
    cashdebt = models.FloatField('cashdebt',default='')
    cashflowdebt = models.FloatField('cashflowdebt',default='')
    turnoverrate = models.FloatField('turnoverrate',default='')
    debtratio = models.FloatField('debtratio',default='')
    roegrowth = models.FloatField('roegrowth',default='')
# Create your models here.
# Create your models here.
