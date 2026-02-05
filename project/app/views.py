from django.shortcuts import render,redirect
from app.models import employee
from app.models import add_dept 

# Create your views here.



def landing(req):
    return render(req,'landing.html')
 

def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        if e == 'admin@gmail.com' and p == 'admin':
            req.session['admin_e'] = e
            req.session['admin_p'] = p
            req.session['admin_n'] = 'admin'
            return redirect('admindashboard')
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
    
    
    
    
def Department(req):
    return redirect(req,'landing.html')
    
      
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
    user=add_dept.objects.all()
    return render(req,'admindashboard.html',{'all_department':user})



def all_query(req):
    return render(req,'all_query.html')

def reply(req):
    return render(req,"reply.html")