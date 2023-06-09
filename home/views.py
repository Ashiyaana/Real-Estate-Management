from django.shortcuts import render, HttpResponse, redirect
from home.forms import *
from home.forms import *
from django.contrib.auth import login
from django.urls import path



# Create your views here.
def index(request):
    # return HttpResponse("hello home page")
    return render(request, 'index.html')
    
def aboutus(request):
    return render(request, 'aboutus.html')


def services(request):
    return HttpResponse("hello services page")

def contact(request):
    # return HttpResponse("hello home page")
    return render(request, 'contact.html')


def buy(request):
    # return HttpResponse("hello home page")
    return render(request, 'buy.html')


def insertcontact(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form=contactform()
    return render(request,"contact.html",{'form':form})

def blogview(request):
    blg=blog.objects.all()
    return render(request,"blog.html",{'blg':blg})

def blogsdetail(request,id):
    b=blog.objects.get(id=id)
    return render(request,"blogsdetail.html" ,{'b':b}) 

def shop(request):
    pro=properties.objects.filter(status='approved').order_by('-id')
    return render(request,"shop.html",{'pro':pro})

def shopdetail(request,id):
    s=properties.objects.get(id=id)
    return render(request,"shopdetail.html" ,{'s':s})


def faqview(request):
    f=faq.objects.all()
    return render(request, "faq.html", {'f':f})
    
def signupview(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid(): 
            user=form.save()
            login(request,user)
            return redirect('/')
    else:
        form=signupform()
    return render(request,"registration/signup.html",{'form':form})   
    
def sell(request):
    return render(request,"sell.html")

def insertsell(request):
    if request.method=='POST':
        form=sellform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=sellform()
    return render(request,"sell.html",{'form':form})


def buyview(request):
    pro=properties.objects.filter(property_for='sale')
    return render(request,"shop.html",{'pro':pro})


def rentview(request):
    pro=properties.objects.filter(property_for='rent')
    return render(request,"shop.html",{'pro':pro})



def insertcontactus(request):
    if request.method=='POST':
        form=shopdetailform(request.POST)
        email=request.POST.get("email")
        if form.is_valid():
            form.save()
            url='/thankyou/{}'.format(email)
            return redirect(url)
            #url='https://mail.google.com/mail/?view=cm&fs=1&to={}'.format(email)
            #return redirect(url)
    else:
        form=shopdetailform()
    return render(request,"shopdetail.html",{'form':form})

def thankyouview(request,v):
    return render(request,"thankyou.html",{'v':v})

def viewcommentsview(request):
    uid=request.user.id
    c=contactus.objects.select_related('propertyid').filter(propertyid__userid=uid)
    return render(request,"name.html",{'c':c})