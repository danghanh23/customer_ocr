from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
import json
from home.api.customer_SF_api import getListCustomerSF, get1CustomerSF, editCustomerSF,deleteCustomerSFApi, createCustomerSFApi
from .forms import CustomerForm, RegistrationForm
from django.contrib.auth import logout, login
import requests
from datetime import datetime
# Create your views here.
def index(request):
    data = {'Customers' : getListCustomerSF(request)}
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
    if request.method == 'POST':
        try:
            createCustomerSFApi(request)
            return HttpResponseRedirect('/')
        except Exception as e:
            print(e)
            return  render(request, 'pages/add_customer.html')
    return render(request, 'pages/add_customer.html')

def deleteCustomer(request, pk):
    try:
        deleteCustomerSFApi(request, pk)
        return HttpResponseRedirect('/')
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/')

def showCustomer(request, pk):
    try:
        obj = get1CustomerSF(request, pk)
        return render(request, 'pages/show_customer.html', {
            'customer': json.dumps(obj.to_json(), indent=4, sort_keys=True, default=str),
            "customerGender": obj.sex,
            "customerPk": str(obj.id)
            })
    except Exception as e:
        return HttpResponseRedirect('/')
    
    
def updateCustomer(request, pk):
    try:
        editCustomerSF(request, pk)
        return HttpResponseRedirect('/')
    except Exception as e:
        print("Cannot update customer ERROR!!!")
        return HttpResponseRedirect('/')
