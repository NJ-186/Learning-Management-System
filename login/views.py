from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else: 
            messages.error(request,'Invalid Credentials')
            return redirect('sign_in')
    else:
        return render(request, 'sign_in.html')

def sign_up(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['emailaddress']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username taken')
                return redirect('sign_up')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email taken')
                return redirect('sign_up')
            else:
                user = User.objects.create_user(first_name = firstname, last_name = lastname, email = email, username = username,password = password1)
                user.save()
                return redirect('sign_in')
        
        else:
            messages.error(request,'Password not matching')
            return redirect('sign_up')

    else:
        return render(request,'sign_up.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def terms_of_use(request):
    return render(request, 'terms_of_use.html')

def sign_up_steps(request):
    return render(request, 'sign_up_steps.html')








def index(request):
    return render(request, 'index.html')

def my_instructor_profile_view(request):
    return render(request, 'my_instructor_profile_view.html')

def instructor_dashboard(request):
    return render(request, 'instructor_dashboard.html')

def about_us(request):
    return render(request, 'about_us.html')

def our_blog(request):
    return render(request, 'our_blog.html')

def press(request):
    return render(request, 'press.html')

def help(request):
    return render(request, 'help.html')

def coming_soon(request):
    return render(request, 'coming_soon.html')
    
def contact_us(request):
    return render(request, 'contact_us.html')

def career(request):
    return render(request, 'career.html')

def create_new_course(request):
    return render(request, 'create_new_course.html')

def instructor_messages(request):
    return render(request, 'instructor_messages.html')

def create_new_course(request):
    return render(request, 'create_new_course.html')

def create_new_course(request):
    return render(request, 'create_new_course.html')

def create_new_course(request):
    return render(request, 'create_new_course.html')

def create_new_course(request):
    return render(request, 'create_new_course.html')

def create_new_course(request):
    return render(request, 'create_new_course.html')

def create_new_course(request):
    return render(request, 'create_new_course.html')
