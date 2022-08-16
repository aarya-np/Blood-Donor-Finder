from turtle import update
from unicodedata import name
from django.shortcuts import redirect, render, HttpResponse
from home.models import Donor, listofbank, cbtcbb,bhaktapurbloodbank,tuhbb
from home.models import Usernamepasswords,Notice
from django.contrib.auth.models import auth, User
# Create your views here.
def index(request):
    notice_list=Notice.objects.all()
    return render(request,'index.html',{'notice_list':notice_list})
    #return HttpResponse("notice page")
def donorlist(request):
    if request.method=="POST":
        mytype=request.POST['mytype']
        if mytype=='A+':
            donor_list=Donor.objects.filter(mytype='A+') 
            #DO NOT USE GET AT ALL. USE FILTER
            return render(request,'donorlist.html',{'donor_list':donor_list})
        elif mytype=='A-':
            donor_list=Donor.objects.filter(mytype='A-') 
            #DO NOT USE GET AT ALL. USE FILTER
            return render(request,'donorlist.html',{'donor_list':donor_list})
        elif mytype=='B+':
            donor_list=Donor.objects.filter(mytype='B+') 
            #DO NOT USE GET AT ALL. USE FILTER
            return render(request,'donorlist.html',{'donor_list':donor_list})
        elif mytype=='B-':
            donor_list=Donor.objects.filter(mytype='B-') 
            #DO NOT USE GET AT ALL. USE FILTER
            return render(request,'donorlist.html',{'donor_list':donor_list})
        elif mytype=='O+':
            donor_list=Donor.objects.filter(mytype='O+') 
            #DO NOT USE GET AT ALL. USE FILTER
            return render(request,'donorlist.html',{'donor_list':donor_list})
        elif mytype=='O-':
            donor_list=Donor.objects.filter(mytype='O-') 
            #DO NOT USE GET AT ALL. USE FILTER
            return render(request,'donorlist.html',{'donor_list':donor_list})
        elif mytype=='AB+':
            donor_list=Donor.objects.filter(mytype='AB+') 
            #DO NOT USE GET AT ALL. USE FILTER
            return render(request,'donorlist.html',{'donor_list':donor_list})
        elif mytype=='AB-':
            donor_list=Donor.objects.filter(mytype='AB-') 
            #DO NOT USE GET AT ALL. USE FILTER
            return render(request,'donorlist.html',{'donor_list':donor_list})
    return render(request,'donorlist.html')
def bloodbanks(request):
    bbl_list=listofbank.objects.all()
    return render(request,'bloodbanks.html',{'bbl_list':bbl_list})

    # return render(request,'bloodbanks.html')
def registration(request):
    if request.method=="POST":
        print("This is post")
        myfirstname=request.POST['myfirstname']
        mylastname=request.POST['mylastname']
        mydistrict=request.POST['mydistrict']
        myphone=request.POST['myphone']
        mytype=request.POST['mytype']
        myage=request.POST['myage']
        Eligible=request.POST['Eligible']
        terms=request.POST['terms']
        print(myfirstname,mylastname,mydistrict,myphone,mytype,myage)
        ins=Donor(myfirstname=myfirstname, mylastname=mylastname, mydistrict=mydistrict,myphone=myphone,mytype=mytype,myage=myage)
        ins.save()
        print("the data has been written")
    return render(request,'registration.html')
def donatenow(request):
    return render(request,'donatenow.html')
def bloodbanklogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if username=='aarya.np':
            if password=='9860427451':
               return render(request,'changedata.html')
    return render (request, 'bloodbanklogin.html')
def changedata(request):
    if request.method=="POST":

        bankid=request.POST.get('bankid')
        Aplus=request.POST.get('Aplus')
        Aminus=request.POST.get('Aminus')
        Bplus=request.POST.get('Bplus')
        Bminus=request.POST.get('Bminus')
        ABplus=request.POST.get('ABplus')
        ABminus=request.POST.get('ABminus')
        Oplus=request.POST.get('Oplus')
        Ominus=request.POST.get('Ominus')
        if bankid=='1':
           bhaktapurbloodbank.objects.filter(bankid='1').delete()
           bbb=bhaktapurbloodbank(bankid='1',Aplus=Aplus, Aminus=Aminus, Bplus=Bplus, Bminus=Bminus, ABplus=ABplus, ABminus=ABminus, Oplus=Oplus, Ominus=Ominus)
           bbb.save()
        elif bankid=='2':
           cbtcbb.objects.filter(bankid='2').delete()
           bbb=cbtcbb(bankid='2',Aplus=Aplus, Aminus=Aminus, Bplus=Bplus, Bminus=Bminus, ABplus=ABplus, ABminus=ABminus, Oplus=Oplus, Ominus=Ominus)
           bbb.save()
        elif bankid=='3':
            tuhbb.objects.filter(bankid='3').delete()
            bbb=tuhbb(bankid='3',Aplus=Aplus, Aminus=Aminus, Bplus=Bplus, Bminus=Bminus, ABplus=ABplus, ABminus=ABminus, Oplus=Oplus, Ominus=Ominus)
            bbb.save()
        return render(request, 'changedata.html')




def bhaktapurbb(request):
    bbb_list=bhaktapurbloodbank.objects.all()
    return render(request,'bhaktapurbb.html',{'bbb_list':bbb_list})
def cbtc(request):
    bbb_list=cbtcbb.objects.all()
    return render(request,'cbtc.html',{'bbb_list':bbb_list})
def tuh(request):
    bbb_list=tuhbb.objects.all()
    return render(request,'tuh.html',{'bbb_list':bbb_list})