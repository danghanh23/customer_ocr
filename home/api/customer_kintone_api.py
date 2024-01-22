from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
import json
from home.models import Customer, CustomerKintone
from django.contrib.auth import logout, login
import requests
from datetime import datetime
listModelKintone = []
def getListCustomer():
    list = []
    url = 'https://2xoympzg0muc.cybozu.com/k/v1/records.json'
    
    
    header = {
    "Content-Type":"application/json",
    "X-Cybozu-API-Token":"CDCsGSA02YCWzRLfBWSI7NqHuvjHEh1vcvOAEYn7",
    "X-Cybozu-Authorization":"bGVkYW5naGFuaEBnLmRlbnNhbi1naW56YS5jby5qcDpIYW5oMTk5OQ==",
    }
    payload = {   
    "app" : 4
    }
    result = requests.get(url,  data=json.dumps(payload), headers=header)
    
    if result.status_code == 200:
        records = result.json().get('records', [])
    else:
        records = []
    try:
        for item in records:
            customerKintone =  CustomerKintone.convertJsonToModel(item)
            list.append(customerKintone)
            list
    except Exception as e:
        print(e)
    list = sorted(list, key=lambda x: x.id, reverse=True)
    listModelKintone = list
    return list

listModelKintone = getListCustomer()

def find_by_id(id):
    list = getListCustomer()
    for item in list:
        if item.id == id:
            return item
    
def editCustomer(id, request):
    url = 'https://2xoympzg0muc.cybozu.com/k/v1/record.json'
    
    header = {
    "Content-Type":"application/json",
    "X-Cybozu-API-Token":"CDCsGSA02YCWzRLfBWSI7NqHuvjHEh1vcvOAEYn7",
    "X-Cybozu-Authorization":"bGVkYW5naGFuaEBnLmRlbnNhbi1naW56YS5jby5qcDpIYW5oMTk5OQ==",
    }
    payload = {
        "app": 4,
        "id": int(id),
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
    result = requests.put(url,  data=json.dumps(payload), headers=header)
    
    if result.status_code == 200:
        listModelKintone = getListCustomer()
        print("Update customer success")
    else:
        print("Cannot update customer ERROR!!!")

