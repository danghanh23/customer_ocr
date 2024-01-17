from django.shortcuts import render
from django.http import HttpResponseRedirect

from home.models import Customer
from .forms import CustomerForm, RegistrationForm
from django.contrib.auth import logout, login
# Create your views here.
def index(request):
    data = {'Customers' :Customer.objects.all().order_by("-register_date") }
    context = {'data': data}
    return render(request, 'pages/home.html', data)

def contact(request):
    return render(request, 'pages/contact.html')

def error(request):
    return render(request, 'pages/error.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})

def logoutCustom(request):
    logout(request)
    return HttpResponseRedirect('/')

def loginCustom(request):
    login(request)
    return render(request, 'pages/register.html', {'form': form})

def gotoRegister(request):
    HttpResponseRedirect('/')
    register(request)
    
    
def addCustomer(request):
    print("xxxxxxxxxxxxxxxxx2")
    # form = CustomerForm()
    # if request.method == 'POST':
    #     form = CustomerForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/')
    return render(request, 'pages/add_customer.html')

def addCustomerxx(request):
    print("xxxxxxxxxxxxxxxxx111111")
    print(request.GET.get('champion_code'))
    return HttpResponseRedirect('/')
   
    
    