from django.shortcuts import render,redirect
from django.http import HttpResponse
from authapp.models import User
from django.contrib.auth import authenticate, login, logout
from decouple import config


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            return HttpResponse('find User')
        else:
            return HttpResponse('not Found')
        #     if user.is_active:
        #         login(request, user)
        #         # Redirect to your desired page after login
        #         if request.user.is_employee:
        #             try:
        #                 subsidiary = request.user.employees.subsidiary
        #                 return redirect(subsidiary.slug + "/employee/")
        #             except:
        #                 messages.error(request, "Profile Incompletea!")
        #         elif request.user.is_client:
        #             try:
        #                 subsidiary = request.user.clients.subsidiary
        #                 return redirect(subsidiary.slug + "/client/")
        #             except:
        #                 messages.error(request, "Profile Incomplete!")
        #         elif request.user.is_superuser:
        #             try:
        #                 # subsidiary = request.user.clients.subsidiary
        #                 return redirect("/admin/")
        #             except:
        #                 messages.error(request, "Profile Incomplete!")
        #         else:
        #             messages.error(request, "You Have No Any Subsidiry")
        #     else:
        #         messages.error(request, "Your account is not active.")
        # else:
        #     messages.error(request, "Invalid Email/Username or Password.")
    data = {"app_name": config('APP_NAME')}
    # Create a template named 'login.html'
    return render(request, "auth/login.html", data)



def error_404(request):
    return render(request, "404.html")

