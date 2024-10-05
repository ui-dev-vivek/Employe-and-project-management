from django.shortcuts import render,redirect
from django.http import HttpResponse
from authapp.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib import messages
from decouple import config
from .forms import *

def user_login(request):
    data={}
    data['app_name']= config('APP_NAME')    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
        else:
            data['form']=form
            return render(request, 'auth/login.html', data)        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)             
                if request.user.is_employee:
                    try:
                        subsidiary = request.user.employees.subsidiary
                        return redirect(subsidiary.slug + "/employee/")
                    except:
                        messages.error(request, "Profile Incompletea!")
                elif request.user.is_client:
                    try:
                        subsidiary = request.user.clients.subsidiary
                        return redirect(subsidiary.slug + "/client/")
                    except:
                        messages.error(request, "Profile Incomplete!")
                elif request.user.is_superuser:
                    try:
                        # subsidiary = request.user.clients.subsidiary
                        return redirect("/admin/")
                    except:
                        messages.error(request, "Profile Incomplete!")
                else:
                    messages.error(request, "You Have No Any Subsidiry")
            else:
                messages.error(request, "Your account is not active.")
        else:
            messages.error(request, "Invalid Email/Username or Password.")
    data['form'] = LoginForm()
  
    return render(request, "auth/login.html", data)


def user_logout(request):
    logout(request)
    return redirect("/")


def forgot_password(request):
    data={'app_name':config('APP_NAME')}
    if request.method=='POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email=request.POST.get('email')
        else:
            data['form'] = form
            return render(request, 'auth/forgot_password.html', data)          
           
        
        try:
            user=User.objects.get(email=email)
            token=default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link=request.build_absolute_uri('/')+ f"reset-password/{uid}/{token}/"
            print(reset_link)
            # user_name=user.first_name + user.last_name
            # Send the email using the HTML template
            # subject = 'Reset Your Password'
            # message = f'Click the link to reset your password: {reset_link}'
            # from_email = 'your-email@gmail.com'  # Use the same email as configured in settings.py
            # recipient_list = [email]

            # send_mail(
            #     subject,
            #     message,
            #     from_email,
            #     recipient_list,
            #     fail_silently=False,
            #     html_message=render_to_string('emails/password_reset_email.html', {'reset_link': reset_link,'name':user_name}),
            # )
            messages.success(request, "Reset link send on register email.")            
        except:
            messages.error(request, "You are not register.")
        data['form']=ForgotPasswordForm()
    return render(request,'auth/forgot_password.html',data)

def reset_password(request,uidb64,token):
    uid=urlsafe_base64_decode(uidb64)
    try:
        user=User.objects.get(pk=uid)
        if user and default_token_generator.check_token(user,token):
            return render(request, "auth/reset_password.html")
            
    except:
        messages.error(request,'Password reset link link is invalied or expired. send agen.')    
        return redirect('auth.forgot')
def redirect_login(request):
    return redirect("/")


def error_404(request):
    return render(request, "404.html")


