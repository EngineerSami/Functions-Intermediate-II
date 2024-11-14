# login_app/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from .models import User

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        try:

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                confirm_password=confirm_password
            )
            messages.success(request, "Successfully registered!")
            request.session['user_id'] = user.id
            return redirect('success')
        except ValidationError as e:

            for error in e.messages:
                messages.error(request, error)
            return redirect('register')

    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                messages.success(request, "Successfully logged in!")
                return redirect('success')
            else:
                messages.error(request, "Invalid credentials.")
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
    
    return render(request, 'login.html')

def success(request):
    if 'user_id' not in request.session:
        return redirect('login')
    user = User.objects.get(id=request.session['user_id'])
    return render(request, 'success.html', {'user': user})

def logout_view(request):
    request.session.flush()  
    return redirect('login')
