from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
import json
from home.models import Customer, CustomerSF, CustomerSF, CustomerSF_full
from django.contrib.auth import logout, login
import requests
from datetime import datetime
listModelSF = []
def getListCustomerSF(request):
    list = []
    url = 'https://densancom-dev-ed.develop.my.salesforce.com/services/data/v52.0/sobjects/AppData__c'
    header = {
    "Content-Type":"application/json",
    "Authorization":"Bearer " + str( request.session.get('token', 'Guest')),
    "Cookie":"BrowserId=50aM9LjREe6XJKUSR7MzXA; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1",
    }
 
    result = requests.get(url, headers=header)
    if result.status_code == 200:
        records = result.json().get('recentItems', [])
    elif result.status_code == 401:
        getToken(request)
        getListCustomerSF(request)
    else:
        records = []
    try:
        for item in records:
            customerSF =  CustomerSF.convertJsonToModel(item)
            list.append(customerSF)
            list
    except Exception as e:
        print(e)
    list = sorted(list, key=lambda x: x.id, reverse=True)
    return list

def getToken(request):
    url = 'https://login.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9fe4g9fhX0E7sLucpHImPhvvgKo.bSf9MoAeKWEJYDCMCf2B0hIwplxi2YeXTxezMuMVEqJbFuPQuwbPH&client_secret=C48AB0E23BDB672A49E20C346728B323B3DFB0B1B58EF97B3E54E4A66DE30721&username=ledanghanh_dev@g.densan-ginza.co.jp&password=Hanh1999'
    header = {
    "Content-Type":"application/json",
    "Cookie":"BrowserId=50aM9LjREe6XJKUSR7MzXA; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1",
    }
    result = requests.post(url, headers=header)
    if result.status_code == 200:
        request.session['token'] = result.json().get('access_token')
    else:
        request.session['token'] = ""
    

# listModelSF = getListCustomerSF()

def get1CustomerSF(request, id):
    url = "https://densancom-dev-ed.develop.my.salesforce.com/services/data/v52.0/sobjects/AppData__c/"+ str(id)
    header = {
    "Content-Type":"application/json",
    "Authorization":"Bearer " + str( request.session.get('token', 'Guest')),
    "Cookie":"BrowserId=50aM9LjREe6XJKUSR7MzXA; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1",
    }
 
    result = requests.get(url, headers=header)
    
    if result.status_code == 200:
        record = result.json()
        return CustomerSF_full.convertJsonToModel(record)
    elif result.status_code == 401:
        getToken(request)
        get1CustomerSF(request, id)
    else:
        print("Cannot update customer ERROR!!!")
        


def find_by_id(id):
    list = getListCustomerSF()
    for item in list:
        if item.id == id:
            return item
    
def editCustomerSF(request, id):
    url = 'https://densancom-dev-ed.develop.my.salesforce.com/services/data/v52.0/sobjects/AppData__c/'+ str(id)
    
    header = {
    "Content-Type":"application/json",
    "Authorization":"Bearer " + str( request.session.get('token', 'Guest')),
    "Cookie":"BrowserId=50aM9LjREe6XJKUSR7MzXA; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1",
    }
    payload = {
        "Name": request.POST.get('data_name') if request.POST.get('data_name') != '' else "",
        "plan_code__c": request.POST.get('plan') if request.POST.get('plan') != '' else "",
        "option_code__c": request.POST.get('option') if request.POST.get('option') != '' else "",
        "campaign_code__c": request.POST.get('campaign') if request.POST.get('campaign') != '' else "",
        "app_date__c": request.POST.get('register_date') if request.POST.get('register_date') != '' else "",
        "name__c": request.POST.get('name') if request.POST.get('name') != '' else "",
        "name_kana__c": request.POST.get('name_kata') if request.POST.get('name_kata') != '' else "",
        
        "sex__c": request.POST.get('gender') if request.POST.get('gender') != '' else "",
        "birthday__c": request.POST.get('birthday') if request.POST.get('birthday') != '' else "",
        "post_code__c": request.POST.get('postal_code') if request.POST.get('postal_code') != '' else "",
        "address__c": request.POST.get('address') if request.POST.get('address') != '' else "",
        "phone_number__c": request.POST.get('phone_number') if request.POST.get('phone_number') != '' else "",
        "mail_address__c": request.POST.get('email') if request.POST.get('email') != '' else "",
        "remarks__c": request.POST.get('note') if request.POST.get('note') != '' else "",
        "status__c": request.POST.get('state') if request.POST.get('state') != '' else "",
    }
    result = requests.patch(url,  data=json.dumps(payload), headers=header)
    
    if result.status_code == 204:
        print("Update customer success")
    elif result.status_code == 401:
        getToken(request)
        editCustomerSF(request, id)
    else:
        print("Cannot update customer ERROR!!!")
        
        
def deleteCustomerApi(id):
    url = 'https://2xoympzg0muc.cybozu.com/k/v1/records.json'
    header = {
    "Content-Type":"application/json",
    "X-Cybozu-API-Token":"CDCsGSA02YCWzRLfBWSI7NqHuvjHEh1vcvOAEYn7",
    "X-Cybozu-Authorization":"bGVkYW5naGFuaEBnLmRlbnNhbi1naW56YS5jby5qcDpIYW5oMTk5OQ==",
    }
    payload = {
        "app": 4,
        "ids": [int(id)],
    }
    result = requests.delete(url,  data=json.dumps(payload), headers=header)
    
    if result.status_code == 200:
        print("Delete customer success")
    else:
        print("Cannot delete customer ERROR!!!")


def createCustomerApi(request):
    url = 'https://2xoympzg0muc.cybozu.com/k/v1/record.json'
    
    header = {
    "Content-Type":"application/json",
    "X-Cybozu-API-Token":"CDCsGSA02YCWzRLfBWSI7NqHuvjHEh1vcvOAEYn7",
    "X-Cybozu-Authorization":"bGVkYW5naGFuaEBnLmRlbnNhbi1naW56YS5jby5qcDpIYW5oMTk5OQ==",
    }
    payload = {
        "app": 4,
        "record": {
            "register_date": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('register_date')
                },
            "plan": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('plan')
                },
            "campaign": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('campaign')
                },
            "option": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('option')
                },
            "first_name":{
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('first_name')
                },
            "last_name": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('last_name')
                },
            
            "first_name_kata": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('first_name_kata')
                },
            "last_name_kata": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('last_name_kata')
                },
            "gender": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('gender')
                },
            "birthday": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('birthday')
                },
            "country": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('country')
                },
            "zip_code": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('zip_code')
                },
            "state_province": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('state_province')
                },
            "city": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('city')
                },
            
            "street": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('street')
                },
            "phone_number": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('phone_number')
                },
            "email": {
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('email')
                },
            "note":{
                "type": "SINGLE_LINE_TEXT",
                "value": request.POST.get('note')
                }
        }
    }
    result = requests.post(url,  data=json.dumps(payload), headers=header)
    
    if result.status_code == 200:
        listModelSF = getListCustomerSF()
        print("Create customer success")
    else:
        print("Cannot Create customer ERROR!!!")
