from django.shortcuts import render, redirect

# Create your views here.
from .forms import CreateUserForm, LoginForm, addProduct, Product

from django.http import HttpResponse

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Product


@login_required(login_url="login")
def landingPage(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, "landingPage.html", context=context)

def registerPage(request):

    form = CreateUserForm()

    if request.method == "POST":
        print("this is working")
        form = CreateUserForm(data=request.POST)

        print(form.is_valid())
        for i in form:
            print(i.errors)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("login")

    context = {'form' : form}
    return render(request, "registerPage.html", context=context)

def loginPage(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)
        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if(user is not None):
                auth.login(request, user)
                print("redirecting...")
                return redirect("landing")

    context = {'form' : form}

    return render(request, 'loginPage.html', context=context)

@login_required(login_url="login")
def user_logout(request):
    
    auth.logout(request)

    return redirect("login")

@login_required(login_url="login")
def display_page(request):
    products = Product.objects.all()

    context = {'products' : products}

    return render(request, 'displayItem.html', context=context)

@login_required(login_url="login")
def display_payment(request):
    return render(request, 'paymentDetail.html')

@login_required(login_url="login")
def create_product(request):
    if request.method == 'POST':
        form = addProduct(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect("display")
    else:
        form = addProduct()

    context = {'form': form}
    return render(request, 'uploadItem.html', context=context)

@login_required(login_url="login")
def detail_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'detailProduct.html', {'data':product})

@login_required(login_url="login")
def display_profile(request):
    return render(request, 'profileSettings.html')

