from django.shortcuts import render,redirect
from app.models import employee
from app.models import add_dept,querys

# Create your views here.



def landing(req):
    return render(req,'landing.html')
 
def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        if e == 'admin@gmail.com' and p == 'admin':
            req.session['admin_n'] = 'admin'
            return redirect('admindashboard')
        else :
            user=employee.objects.filter(email=e) 
            if user:
                udata=employee.objects.get(email=e)
                if udata.email==e and udata.lname==p:
                    return redirect('userpanel')        
    else:
        x={ 'g':"wrong passord or username"}
        return render(req,'login.html',{'data':x})
    return render(req, 'login.html')

def admindashboard(req):
    # Admin Session Check
    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
        return render(req, 'admindashboard.html', {'data': a_data})
    else:
        return redirect('login')
    


def logout(req):
    if 'admin_e' in req.session:
        req.session.flush()
        return redirect('login')
    else:
        return redirect('login')
    
    
    
    
      
def add_employee(req):
    
    return render(req,'admindashboard.html',{'add_employee':True})

def add(req):
    if req.method=="POST":
        fname=req.POST.get('fname')
        lname=req.POST.get('lname')
        email=req.POST.get('email')
        Department=req.POST.get('dept')
        
        user=employee.objects.filter(email=email)
        if user:
            return render(req,'admindashboard.html',{'add_employee':True})
        else:
            employee.objects.create(fname=fname,lname=lname,email=email,dept=Department)
            return render(req,'admindashboard.html',{'add_employee':True})
        
def all_employee(req):
    user =employee.objects.all()
    return render(req,'admindashboard.html',{'data':user,'all_employee':True})

def add_department(req):
        return render(req,'admindashboard.html',{'add_department':True})  


def add_d(req):
    if req.method == "POST":
        d = req.POST.get('department')
        h = req.POST.get('h_department')
        add_dept.objects.create(department=d, h_department=h)
        return render(req, 'admindashboard.html', {'add_department': True})

    else:
        return render(req, 'admindashboard.html')

def all_department(req):
    uuser=add_dept.objects.all()
    return render(req,'admindashboard.html',{'all_department':uuser})

# usrpanel

def userpanel(req):
    return render(req,'userpanel.html')

def submit_q(req):
    if req.method=="POST":
        n=req.POST.get('name')
        e=req.POST.get('email')
        d=req.POST.get('department')
        q=req.POST.get('query')
        querys.objects.create(name=n,email=e,department=d,query=q)
        return render(req,'userpanel.html',{'submit_q':True})
    return render(req,'userpanel.html',{'submit_q':True})
    
    
def show_q(req):
    data1=querys.objects.all()
    return render(req,'userpanel.html',{'show_q':True,'data1':data1})
    


def all_q(req):
    dataa=querys.objects.all()
    return render(req,'admindashboard.html',{'all_q':dataa})



def pending(req):
    return render(req,'userpanel.html',{'pending':True})


def pending_q(req):
    data=querys.objects.all()
    return render(req,"userpanel.html",{'pending_q':True,'data':data})

    

def edit(req,pk):
    data=querys.objects.filter(id=pk)
    dq=querys.objects.get(id=pk)
    return render(req,"userpanel.html",{'edit':True,'data':dq})


def delete(req,pk):
    data=querys.objects.filter(id=pk)
    data.delete()
    return render(req,'userpanel.html',{'show_q':True ,'data':data})
