from django.shortcuts import render, redirect,reverse
import datetime
from . models import Enquiry,Customer,Login
from django.core.exceptions import ObjectDoesNotExist
from . smssender import sendsms
# Create your views here.
def index(request):
     return render(request, "index.html")
def aboutus(request):
     return render(request, "aboutus.html")
def login(request):
     if request.method=="POST":
          userid=request.POST['userid']
          password=request.POST['password']

          try:
               obj=Login.objects.get(userid=userid,password=password)
               if obj is not None:
                    if obj.usertype=="customer":
                         request.session["userid"]=userid
                         return redirect(reverse("customerapp:customerhome"))
                    elif obj.usertype=="admin":
                         request.session["adminid"]=userid
                         return redirect(reverse("adminapp:adminhome"))
          except ObjectDoesNotExist:               
               msg="Invalid User"
          return render(request,"login.html",{"msg":msg})
                         
     return render(request, "login.html")
def registration(request):
     if request.method=="POST":
          name=request.POST['name']
          gender=request.POST['gender']
          address=request.POST['address']
          contactno=request.POST['contactno']
          emailaddress=request.POST['emailaddress']
          password=request.POST['password']
          confirmpassword=request.POST['confirmpassword']
          regdate=datetime.datetime.today()
          usertype='customer'
          if password==confirmpassword:
               cust=Customer(name=name,gender=gender,address=address,emailaddress=emailaddress,contactno=contactno,regdate=regdate)
               cust.save()
               valid=Login(userid=emailaddress,password=password,usertype=usertype)
               valid.save()
               return render(request,'registration.html',{"msg":"Registration Successfully"})
          else:
               return render(request,"registration.html",{"msg":"Password and Confirm Password does not match"})
     return render(request, "registration.html")
def contactus(request):
     if request.method=="POST":
          name=request.POST['name']
          contactno=request.POST['contactno']
          emailaddress=request.POST['emailaddress']
          subject=request.POST['subject']
          message=request.POST['message']
          posteddate=datetime.datetime.today()
          enq=Enquiry(name=name,contactno=contactno,emailaddress=emailaddress,subject=subject,message=message,posteddate=posteddate)
          enq.save()
          sendsms(contactno)
          return render(request,"contactus.html",{"msg":"Enquiry is saved"})
     return render(request, "contactus.html")