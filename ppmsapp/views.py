import os
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from ppmsapp.models import *
from tkinter import messagebox
from django.contrib import messages

# Create your views here.
def home(request): 
    prd = Report.objects.all()
    return render(request,"home.html",{"prd":prd})

def Eadmin(request):
    return render(request,"admin.html")

def Euser(request):
    return render(request,'employee.html')

def loginpage(request):
    return render(request,'login.html')

def signuppage(request):
    return render(request,'signup.html')

def add_report(request):
    catg = Category.objects.all()
    return render(request,'admin/areport.html',{'catg':catg})

def showreport(request):
    scatg =Category.objects.all()
    sprd = Report.objects.all()
    return render(request,'admin/sreport.html',{'cat':scatg,'prod':sprd})

def edit_report(request,od):
    ecatg = Category.objects.all()
    prd = Report.objects.get(id=od)
    return render(request,'admin/ereport.html',{'ecatg':ecatg,'prod':prd})

def add_category(request):
    return render(request,'admin/acategory.html')

def show_category(request):
    catgry = Category.objects.all()
    return render(request,'admin/showcateg.html',{'catg':catgry})

def edit_category(request,od):
    catgry = Category.objects.get(id=od)
    return render(request,'admin/ecategory.html',{'catg':catgry})

def show_user(request): #admin.....
    usr = Employee.objects.all()
    return render(request,'admin/showusers.html',{'user':usr})

def register(request):
    rreg=Attendance.objects.all()
    return render(request,'admin/register.html',{'ratten':rreg})

def show_register(request):
    reg=Attendance.objects.all()
    return render(request,'admin/showregister.html',{'sreg':reg})

def tregister(request):
        if request.method == 'POST':
            latten=request.POST['atten']
            lrdob=request.POST['date']
            lshift=request.POST['shift']
            addregister=Attendance(a_attendnce=latten,a_DOB =lrdob,a_post=lshift)
            addregister.save()
            messages.success(request,'Leave has being applied')
            return redirect('register')
        
    
def aleave(request):
    rleave = Leave.objects.all()
    return render(request,'admin/leave.html',{'rleave':rleave})
    
def show_leave(request):
    leav=Leave.objects.all()
    return render(request,'admin/showleave.html',{'sleave':leav})

def tleave(request):
        if request.method == 'POST':
            lreq=request.POST['req']
            lreas=request.POST['reas']
            addleave=Leave(l_req=lreq,l_reason=lreas)
            addleave.save()
            messages.success(request,'Leave has being applied')
            return redirect('aleave')

def uprofile(request):
    global u_name
    data = User.objects.get(username=u_name)
    print(data)
    global data1
    data1= Employee.objects.get(e_user=data)
    print(data1)
    return render(request,'employee/profile.html',{'data':data, 'data1':data1})  

def Login(request):
    if request.method== 'POST':
        global u_name
        u_name = request.POST['logname']
        pawd = request.POST['passw']
        log= auth.authenticate(username = u_name, password = pawd)
        if log is not None:
            if log.is_staff:
                auth.login(request,log)
                return redirect('Eadmin')
            else:
                auth.login(request,log)
                return redirect('Euser')
        else:
            print("User name or password does not match. Try again.")
            return redirect('Login')
        
def Signup(request):
    if request.method == 'POST':
        Fname = request.POST['fname']
        Lname= request.POST['lname']
        usernam= request.POST['uname']
        Email = request.POST['E-mail']
        Address=request.POST['adds']
        Post=request.POST['post']
        Age=request.POST['Age']
        pnum = request.POST['tphone']
        paswd = request.POST['pswd']
        cpaswd = request.POST['cpswd']
        if paswd == cpaswd:
            if User.objects.filter(password = paswd).exists():
                print("This user name already exists")
                return redirect('signuppage')
            else:
                user = User.objects.create_user(username=usernam,first_name=Fname,
                            last_name=Lname,email=Email,password=paswd)
                user.save()
                employee=User.objects.get(username=usernam) # for adding id in foriegn key column
                custm = Employee(e_fname=Fname,e_lname=Lname,e_address=Address,
                                               e_age=Age,e_post=Post,e_phone_numbr=pnum,
                                               e_email=Email,e_user=employee)
                custm.save()
                return redirect('home')
        else:
            print("password id not matc try agian!")
            return redirect('home')
        
def eprofile(request):
    if request.method=='POST':

        us = User.objects.get(username=u_name)
        us.first_name=request.POST['pfname']
        us.last_name=request.POST['plname']
        us.save()
        data1.e_fname = request.POST['pfname']
        data1.e_lname = request.POST['plname']
        data1.e_phone_numbr = request.POST['phnmbr']
        data1.e_address = request.POST['adds']
        data1.e_post = request.POST['post']
        data1.e_age = request.POST['age']
        # data1.e_photo = request.POST['photo']
        try:
            if len(request.FILES)!=0:
                try:
                    if len(data1.e_photo)>0:
                        os.remove(data1.e_photo.path)
                    data1.e_photo= request.FILES['photo']
                except:
                    None
                data1.e_photo = request.FILES['photo']
        except:
            data1.e_photo = request.FILES['photo']
        data1.save()
        return redirect('Euser')
    
def a_category(request):
    if request.method == 'POST':
        pcatg = request.POST['pcatgr']
        pri = request.POST['pric']
        st = request.POST['stoc']
        catg = Category(product_category= pcatg, product_price = pri,product_stock = st)
        catg.save()
        return redirect('add_category')

def e_category(request,od):
    if request.method == 'POST':
        catg = Category.objects.get(id=od)
        catg.product_category = request.POST['npcatgr']
        catg.product_price = request.POST['npri']
        catg.product_stock = request.POST['nst']
        catg.save()
        return redirect('show_category')
 
def a_report(request):
    if request.method == 'POST':
        pname = request.POST['prname']
        pdes = request.POST['prdesc']
        date= request.POST['prdate']
        pstock = request.POST['prstock']
        catg = request.POST['adcatg']
        cat = Category.objects.get(id=catg)
        add = Report(r_name=pname,r_details=pdes,
        r_DOB=date,r_quantity=pstock,r_category=cat)
        add.save()
        return redirect('add_report')

def e_report(request,od):
    if request.method == 'POST':
        prod = Report.objects.get(id=od)
        prod.r_name = request.POST['nprname']
        prod.r_details = request.POST['nprdesc']
        prod.r_DOB = request.POST['nprdate']
        prod.r_quantity = request.POST['nprquanity']
        catg = request.POST['nadcatg']
        cat = Category.objects.get(id=catg)
        prod.r_category = cat
        prod.save()
        return redirect('showreport')

def delete_report(request,od):
    prod=Report.objects.get(id=od) 
    prod.delete()
    return redirect('showreport')

def delete_leave(request,od):
    sleave=Leave.objects.get(id=od)
    sleave.delete()
    return redirect('show_leave')

def delete_register(request,od):
    sreg=Attendance.objects.get(id=od)
    sreg.delete()
    return redirect('show_register')

def deletecust(request,od):
    cust = Employee.objects.get(id=od)
    catm = cust.e_user.id
    usr = User.objects.get(id=catm)
    usr.delete()
    cust.delete()
    return redirect("show_user")

@login_required(login_url='Login')
def Logout(request):
    auth.logout(request)
    return redirect('home')