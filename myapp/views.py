from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import DetailView
from .forms import LoginForm ,RegisterForm
from django.contrib.auth.hashers import make_password

from .models import Product,Login
# Create your views here.

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

def index(request):
    return HttpResponse("Hello hbiba noussair")

def  contact(request):
    x ={'name':"noussair",'age':22}
    return render(request,"index.html",x)

def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        data =  Login(name = name, password =password)
        data.save()
        return redirect('index')
    return render(request,'about.html')


def product(request):
    return render(request,'product/product.html')


def products(request):
    return render(request, 'product/products.html', {'pro': Product.objects.all()})

def phone(request):
    context = {'phone':Product.objects.all().filter(category='phone')}
    # con = {'phone':Product.objects.all().exclude(price=100)}
    return render(request, 'product/phone.html', context)

def forme(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        login = form.save(commit=False)
        login.password = make_password(form.cleaned_data['password'])
        login.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'forme.html', context)

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.password = make_password(form.cleaned_data['password'])
        user.save()
        return redirect('index')
    else:
        print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)