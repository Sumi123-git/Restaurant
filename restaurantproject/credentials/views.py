from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import reserve
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('registration.html')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=email, password=password)
                user.save();
                # return render(request,'login.html')
                # messages.info(request, "user created")
                return render(request,'login.html')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
            return redirect('/')
    return render(request, "registration.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'foodbooking1.html')
        else:
            messages.info(request, "invalid")
            return render(request,'login.html')
    return render(request, "login.html")


# def booking(request):
#     # return HttpResponse("jj")
#     if request.method == "POST":
#         username = request.POST('username')
#         email = request.POST('email')
#         first_name = request.POST('first_name')
#
#         last_name = request.POST('last_name')
#
#         reservations = User.objects.create_user(username=username, first_name=first_name, email=email,
#                                                 last_name=last_name)
#
#         reservations.save()
#         messages.info(request, "order conformed")
#     return render(request,'login.html')
#     return render(request,'foodbooking1.html' )
def booking(request):
    rese1=reserve.objects.all()
    context={
        'items':rese1
    }
    return render(request,'login.html')
    return render(request,'foodbooking1.html',context)

