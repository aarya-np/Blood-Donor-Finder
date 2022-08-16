from datetime import date, datetime, time
from email.policy import default
from importlib.metadata import requires
from multiprocessing.sharedctypes import Value
from operator import mod
from django.db import models
from pytz import timezone

# Create your models here.

class Donor(models.Model):
    myfirstname = models.CharField(max_length=30)
    mylastname = models.CharField(max_length=30)
    mydistrict=models.CharField(max_length=30)
    myphone=models.CharField(max_length=10)
    # myphone=models.CharField(max_length=10)
    mytype=models.CharField(max_length=30)
    myage=models.CharField(max_length=2)
    Eligible=models.BooleanField(default=True)
    terms=models.BooleanField(default=True)
    def __str__(self):
        return self.myfirstname + ' '+ self.mylastname
        #database ma names le represent garcha 
    #models or aru kei ma changes lyayo bhane python manage.py makemigrations run garne, ani feri migrate bhanera run garne, ani balla runserver garne

class Usernamepasswords(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=100)
    

class Notice(models.Model):
    name=models.CharField(max_length=120)
    time=models.DateTimeField(default=datetime.now)
    description=models.TextField(blank=True)

class listofbank(models.Model):
    bankname=models.CharField(max_length=300)
    bankphone=models.CharField(max_length=10)
    locationname=models.CharField(max_length=100)
    location=models.URLField(max_length=200)
    htmlfile=models.CharField(default='none',max_length=200)

class bhaktapurbloodbank(models.Model):
    bankid=models.CharField(default='1',max_length=100)
    Aplus=models.CharField(max_length=30)
    Aminus=models.CharField(max_length=30)
    Bplus=models.CharField(max_length=30)
    Bminus=models.CharField(max_length=30)
    ABplus=models.CharField(max_length=30)
    ABminus=models.CharField(max_length=30)
    Oplus=models.CharField(max_length=30)
    Ominus=models.CharField(max_length=30)

class cbtcbb(models.Model):
    bankid=models.CharField(default='2', max_length=100)
    Aplus=models.CharField(max_length=30)
    Aminus=models.CharField(max_length=30)
    Bplus=models.CharField(max_length=30)
    Bminus=models.CharField(max_length=30)
    ABplus=models.CharField(max_length=30)
    ABminus=models.CharField(max_length=30)
    Oplus=models.CharField(max_length=30)
    Ominus=models.CharField(max_length=30)

class tuhbb(models.Model):
    bankid=models.CharField(default='3', max_length=100)
    Aplus=models.CharField(max_length=30)
    Aminus=models.CharField(max_length=30)
    Bplus=models.CharField(max_length=30)
    Bminus=models.CharField(max_length=30)
    ABplus=models.CharField(max_length=30)
    ABminus=models.CharField(max_length=30)
    Oplus=models.CharField(max_length=30)
    Ominus=models.CharField(max_length=30)

class mwhbb(models.Model):
    bankid=models.CharField(default='4', max_length=100)
    Aplus=models.CharField(max_length=30)
    Aminus=models.CharField(max_length=30)
    Bplus=models.CharField(max_length=30)
    Bminus=models.CharField(max_length=30)
    ABplus=models.CharField(max_length=30)
    ABminus=models.CharField(max_length=30)
    Oplus=models.CharField(max_length=30)
    Ominus=models.CharField(max_length=30)

class bhbb(models.Model):
    bankid=models.CharField(default='5', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class gihbb(models.Model):
    bankid=models.CharField(default='6', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class hhbb(models.Model):
    bankid=models.CharField(default='7', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class nphbb(models.Model):
    bankid=models.CharField(default='8', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class nhbb(models.Model):
    bankid=models.CharField(default='9', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class gmhcbb(models.Model):
    bankid=models.CharField(default='10', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class nmhbb(models.Model):
    bankid=models.CharField(default='11', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class cshbb(models.Model):
    bankid=models.CharField(default='12', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class lbb(models.Model):
    bankid=models.CharField(default='13', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class jbtsbb(models.Model):
    bankid=models.CharField(default='14', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class sbtsbb(models.Model):
    bankid=models.CharField(default='15', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class mrbtsbb(models.Model):
    bankid=models.CharField(default='16', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class dbtsbb(models.Model):
    bankid=models.CharField(default='17', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class pbtsbb(models.Model):
    bankid=models.CharField(default='18', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

class kbtsbb(models.Model):
    bankid=models.CharField(default='19', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)
class dhbb(models.Model):
    bankid=models.CharField(default='20', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)
class crbtsbb(models.Model):
    bankid=models.CharField(default='21', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)
class cmcbtubb(models.Model):
    bankid=models.CharField(default='22', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)
class bpkmchbb(models.Model):
    bankid=models.CharField(default='23', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)
class rbtsbb(models.Model):
    bankid=models.CharField(default='24', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)
class krbtsbb(models.Model):
    bankid=models.CharField(default='25', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)
class dbtsbbb(models.Model):
    bankid=models.CharField(default='26', max_length=100)
    Aplus=models.CharField(default='none',max_length=30)
    Aminus=models.CharField(default='none',max_length=30)
    Bplus=models.CharField(default='none',max_length=30)
    Bminus=models.CharField(default='none',max_length=30)
    ABplus=models.CharField(default='none',max_length=30)
    ABminus=models.CharField(default='none',max_length=30)
    Oplus=models.CharField(default='none',max_length=30)
    Ominus=models.CharField(default='none',max_length=30)

















    










     