from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from crmapp.models import Customer,Login,Enquiry
from customerapp.models import Response,Orders
from . models import Product

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminhome(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            return render(request,"adminhome.html",locals())
    except:
        return redirect("crmapp:login")    
def logout(request):
    try:
        del request.session["adminid"]
        return redirect("crmapp:login")
    except:
        return redirect("crmapp:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewcustomers(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            cust=Customer.objects.all()
            return render(request,"viewcustomers.html",locals())
    except:
        return redirect("crmapp:login")        
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewenquiries(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            enq=Enquiry.objects.all()
            return render(request,"viewenquiries.html",locals())
    except:
        return redirect("crmapp:login")        
    
def delenq(request,id):
    Enquiry.objects.get(id=id).delete()
    return redirect("adminapp:viewenquiries")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewfeedbacks(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            feed=Response.objects.filter(responsetype='feedback')
            return render(request,"viewfeedbacks.html",locals())
    except:
        return redirect("crmapp:login")  
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewcomplaint(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            comp=Response.objects.filter(responsetype='complaint')
            return render(request,"viewcomplaint.html",locals())
    except:
        return redirect("crmapp:login")      
def delcomp(request,id):
    Response.objects.get(id=id).delete()
    return redirect("adminapp:viewcomplaint")
def delfeed(request,id):
    Response.objects.get(id=id).delete()
    return redirect("adminapp:viewfeedbacks")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def changeadminpassword(request):
    # try:
        if request.session['adminid']!=None:
            if request.method=='POST':
                adm=Login.objects.get(userid=request.session['adminid'])
                oldpassword=request.POST['oldpassword']
                newpassword=request.POST['newpassword']
                conpassword=request.POST['conpassword']
                if adm.password==oldpassword:
                    if oldpassword==newpassword:
                        msg="Old password and new password are same"
                    else:
                        if newpassword==conpassword:
                            adm.password=newpassword
                            adm.save()
                            msg="Confirm Changed Successfully"
                        else:
                            msg="Confirm password didnot matched"    
                else:
                    msg="Old password not match"
            return render(request,'changeadminpassword.html',locals())
            
    # except:
        return render('crmapp:login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def product(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
           
            if request.method=="POST":
                productname=request.POST["productname"]
                mfgdate=request.POST["mfgdate"]
                expdate=request.POST["expdate"]
                price=request.POST["price"]
                productpic=request.FILES["productpic"]
                prd=Product(productname=productname,mfgdate=mfgdate,expdate=expdate,price=price,productpic=productpic,avail='true')
                prd.save()
                msg='Product is added'
                return render(request,"product.html",locals())
            return render(request,"product.html",locals())
    except:
        return redirect("crmapp:login")    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewproducts(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            prod=Product.objects.all()
            return render(request,"viewproducts.html",locals())
    except:
        return redirect("crmapp:login")  
       
def delprod(request,id):
    Product.objects.get(id=id).delete()
    return redirect("adminapp:viewproducts")    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewcustorders(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            ord=Orders.objects.all()
            return render(request,"viewcustorders.html",locals())
    except:
        return redirect("crmapp:login")