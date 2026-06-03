from django.shortcuts import render, redirect
from .models import Employee

def signup_view(request):
    if request.method == "POST":
        Employee.objects.create(
            name=request.POST['name'],
            address=request.POST['address'],
            contact=request.POST['contact'],
            emp_id=request.POST['emp_id'],
            department=request.POST['department'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Employee.objects.get(
                username=username,
                password=password
            )

            request.session['user'] = user.username

            return redirect('dashboard')

        except:
            return render(request, 'login.html', {
                'error': 'Invalid Credentials'
            })

    return render(request, 'login.html')


def dashboard_view(request):

    if 'user' not in request.session:
        return redirect('login')

    user = Employee.objects.get(
        username=request.session['user']
    )

    return render(request, 'dashboard.html', {'user': user})


def logout_view(request):

    request.session.flush()

    return redirect('login')