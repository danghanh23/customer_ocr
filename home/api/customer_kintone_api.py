from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
import json
from home.models import Customer, CustomerKintone
from django.contrib.auth import logout, login
import requests
from datetime import datetime


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
    return list

listModelKintone = getListCustomer()

def find_by_id(id):
    for item in listModelKintone:
        if item.id == id:
            return item
    
def editCustomer():
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
    return list


