from django.shortcuts import render,redirect
# from models import Department 

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
    
