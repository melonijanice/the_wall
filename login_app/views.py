from login_app.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request,'register.html')

def register(request):
    errors = User.objects.registration_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
        user_id=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],EmailField=request.POST['email'],password=pw_hash)
        request.session['user_id']=user_id.id
        return redirect('/wall')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context={"User_name":User.objects.get(id=request.session.get('user_id')).first_name}
        return render(request,'success.html',context)

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        user = User.objects.filter(EmailField=request.POST['email'])
        print(user)
        if user:
            logged_user = user[0]
            request.session['user_id']=logged_user.id
            return redirect('/wall')
        else:
            return redirect('/')

def logout(request):
    if request.method=="GET":
        return redirect('/')
    request.session.flush()
    return redirect('/')

        
