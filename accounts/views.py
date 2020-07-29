from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models  import User,auth
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if(password1==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('accounts:register')
            else:
                 user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,email=email)
                 user.save();
                 print('user created')
        else:
            return redirect('accounts:register')
        return redirect('/')

    return render (request,'accounts/register.html')
    
def login(request):
    if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                print('login')
            else:
                messages.error(request,'Invalid credentials')
                return redirect('accounts:login')
    else:
        return render(request,'accounts/login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
        
