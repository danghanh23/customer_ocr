from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
import json
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
    form = CustomerForm()
    if request.method == 'POST':
        try:
            customer = Customer(
            register_date = request.POST.get('register_date'),
            plan = request.POST.get('plan'),
            campaign = request.POST.get('campaign'),
            option = request.POST.get('option'),
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            
            first_name_kata = request.POST.get('first_name_kata'),
            last_name_kata = request.POST.get('last_name_kata'),
            
            gender = request.POST.get('gender'),
            birthday = request.POST.get('birthday'),
            country = request.POST.get('country'),
            zip_code = request.POST.get('zip_code'),
            state_province = request.POST.get('state_province'),
            city = request.POST.get('city'),
            street = request.POST.get('street'),
            
            phone_number = request.POST.get('phone_number'),
            email = request.POST.get('email'),
            note = request.POST.get('note'),
                )
            customer.save()
            customer.unique_error_message
            return HttpResponseRedirect('/')
        except Exception as e:
            print(e)
            return  render(request, 'pages/add_customer.html')
    return render(request, 'pages/add_customer.html')

def deleteCustomer(request, pk):
    obj = get_object_or_404(Customer, pk=pk)
    try:
        obj.delete()
        return HttpResponseRedirect('/')
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/')
    