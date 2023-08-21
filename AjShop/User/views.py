from django.shortcuts import render,redirect
from django.http import HttpResponse
from Admin.models import Category,Product,UserInfo,Payment
from User.models import Mycart,Ordermaster
from django.contrib import messages

# Create your views here.
def homepage(request):
    cats = Category.objects.all()
    gadgets = Product.objects.all()
    return render(request,'homepage.html',{"cats":cats,"gadgets":gadgets})

def login(request):
    if(request.method == "GET"):
        return render(request,'login.html',{})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        try:
            user = UserInfo.objects.get(uname = uname, password = password)
            
        except:
            messages.success(request,'Login Failed')
            return redirect(login)
        else:
            #Create Session
            request.session["uname"]=uname
            return redirect(homepage)

def ShowGad(request,id):
    id = Category.objects.get(id=id)
    cats = Category.objects.all()
    gadgets = Product.objects.filter(cat = id)
    return render (request,'homepage.html',{"cats":cats,"gadgets":gadgets})

def ViewDetails(request,id):
    gadget = Product.objects.get(id=id)
    return render (request,'ViewDetails.html',{'gadget':gadget})

def signup(request):
    if(request.method == "GET"):
        return render(request,"signup.html",{})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = UserInfo(uname,password,email)
        user.save()
        return redirect(homepage)

def signout(request):
    request.session.clear()
    return redirect(homepage)

def addcart(request):
    if(request.method == "POST"):
        if("uname" in request.session):
            #Add to cart
            #user And Product
            gadgetid = request.POST["gadgetid"]
            user = request.session["uname"]
            qty = request.POST["qty"]
            gadget = Product.objects.get(id = gadgetid)
            user = UserInfo.objects.get(uname = user)

            #check for duplicate entry
            try:
                cart = Mycart.objects.get(gadget=gadget,user=user)
            except:
                cart = Mycart()
                cart.user = user
                cart.gadget = gadget
                cart.qty = qty
                cart.save()
            else:
                pass
            return redirect(homepage)
        else:
            return redirect(login)
        
def ShowItems(request):
    uname = request.session["uname"]
    user = UserInfo.objects.get(uname = uname)
    if(request.method == "GET"):
        cartitems = Mycart.objects.filter(user = user)
        total = 0
        for item in cartitems:
            total += item.qty * item.gadget.price
        request.session["total"] = total
        return render(request,'Showcart.html',{"items":cartitems})
    else:
        id = request.POST['gadgetid']
        gadget = Product.objects.get(id = id)
        item = Mycart.objects.get(user=user,gadget=gadget)
        
        qty=request.POST['qty']
        item.qty = qty
        item.save()
        return redirect (ShowItems)
    
def remove(request):
    uname = request.session["uname"]
    user = UserInfo.objects.get(uname = uname)
    id = request.POST['gadgetid']
    gadget = Product.objects.get(id = id)
    item = Mycart.objects.get(user=user,gadget=gadget)
    item.delete()
    return redirect(ShowItems)
    
        
def MakePayment(request):
    if(request.method == "GET"):
        return render(request,'Payment.html',{})
    else:
        cardno = request.POST['cardno']
        cvv = request.POST['cvv']
        exp = request.POST['exp']
        try:
            buyer = Payment.objects.get(cardno=cardno,cvv=cvv,exp=exp)
        except:
            return redirect(MakePayment)
        else:
            #  If it's Match
            owner = Payment.objects.get(cardno='111',cvv='111',exp='12/2025')
            owner.balance += request.session["total"]
            buyer.balance -= request.session['total']
            owner.save()
            buyer.save()
            #Delete all Cart Items

            uname = request.session["uname"]
            user = UserInfo.objects.get(uname = uname)

            order = Ordermaster()
            order.user = user 
            order.amount = request.session["total"]
            #Fetch all Cart Items
            details = ''
            items = Mycart.objects.filter(user=user)
            for item in items:
                details += (item.gadget.pname) + ','
                item.delete()
            order.details = details
            order.save()
            return redirect(homepage)
