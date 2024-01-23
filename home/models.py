from django.db import models
from django.utils import timezone
# Create your models here.
from datetime import datetime

class CustomerSF_full:
    def __init__(self,
    dataName ,
    plan ,
    option ,
    campaign ,
    appDate ,
    name ,
    nameKata ,
    sex ,
    birthday ,
    # post ,
    address ,
    phoneNumber ,
    mailAddress ,
    remarks ,
    status ,
    id  ):
        self.dataName = dataName
        self.plan = plan,
        self.option = option
        self.campaign = campaign
        self.appDate = appDate
        self.name = name
        
        self.nameKata = nameKata
        self.sex = sex
        self.birthday = birthday
        # self.post = post
        self.address = address
        self.phoneNumber = phoneNumber
        self.mailAddress = mailAddress
        self.remarks = remarks
        self.status = status
        self.id = id
    def to_json(self):
        return {
            
            'id': self.id,
            "dataName": self.dataName,
            "plan": self.plan,
            "campaign": self.campaign,
            "option": self.option,
            "appDate": self.appDate,
            "name": self.name,
            "nameKata": self.nameKata,
            
            "sex": self.sex,
            "birthday": self.birthday,
            # "post": self.post,
            "address": self.address,
            "phoneNumber": self.phoneNumber,
            "mailAddress": self.mailAddress,
            "remarks": self.remarks,
            "status": self.status,
        }
    
    def convertJsonToModel(json):
        tmp = json['plan_code__c'] if  json['plan_code__c'] != None else ""
        model = CustomerSF_full(
            id = json['Id'],
            dataName = json['Name'],
            plan = tmp,
            option = json['option_code__c'] if  json['option_code__c'] != None else "",
            campaign = json['campaign_code__c'] if  json['campaign_code__c'] != None else "",
            appDate =  datetime.strptime(json['app_date__c'], "%Y-%m-%d").date() if  json['app_date__c'] != None else "",
            name = json['name__c']  if  json['name__c'] != None else "",
            nameKata = json['name_kana__c']if  json['name_kana__c'] != None else "",
            sex = json['sex__c']if  json['sex__c'] != None else "",
            birthday =  datetime.strptime(json['birthday__c'], "%Y-%m-%d").date() if  json['birthday__c'] != None else "",
            # post = json['address__postalcode__s']if  json['address__postalcode__s'] != None else "",
            address = json['address__c']if  json['address__c'] != None else "",
            phoneNumber = json['phone_number__c']if  json['phone_number__c'] != None else "",
            mailAddress = json['mail_address__c']if  json['mail_address__c'] != None else "",
            remarks = json['remarks__c']if  json['remarks__c'] != None else "",
            status = json['status__c']if  json['status__c'] != None else "",
        )
        model.plan = tmp
        return model
    
class CustomerSF:
    def __init__(self,
    dataName ,
    id  ):
        self.dataName = dataName
        self.id = id
    def convertJsonToModel(json):
        model = CustomerSF(
            id = json['Id'],
            dataName = json['Name'],
        )
        return model
    
    
class CustomerKintone:
    def __init__(self, register_date ,
    plan ,
    campaign ,
    option ,
    first_name ,
    last_name ,
    first_name_kata ,
    last_name_kata ,
    gender ,
    birthday ,
    country ,
    zip_code ,
    state_province ,
    city ,
    street ,
    phone_number ,
    email ,
    note ,
    id  ):
        self.register_date = register_date
        self.plan = plan,
        self.campaign = campaign
        self.option = option
        self.first_name = first_name
        self.last_name = last_name
        
        self.first_name_kata = first_name_kata
        self.last_name_kata = last_name_kata
        
        self.gender = gender
        self.birthday = birthday
        self.country = country
        self.zip_code = zip_code
        self.state_province = state_province
        self.city = city
        self.street = street
        
        self.phone_number = phone_number
        self.email = email
        self.note = note
        self.id = id
    def to_json(self):
        return {
            'id': self.id,
            "register_date": self.register_date,
            "plan": self.plan,
            "campaign": self.campaign,
            "option": self.option,
            "first_name": self.first_name,
            "last_name": self.last_name,
            
            "first_name_kata": self.first_name_kata,
            "last_name_kata": self.last_name_kata,
            "gender": self.gender,
            "birthday": self.birthday,
            "country": self.country,
            "zip_code": self.zip_code,
            "state_province": self.state_province,
            "city": self.city,
            
            "street": self.street,
            "phone_number": self.phone_number,
            "email": self.email,
            "note": self.note,
        }
    
    def convertJsonToModel(json):
        model = CustomerKintone(
            register_date = datetime.strptime(json['register_date']['value'], "%Y-%m-%d").date(),
            plan = json['plan']['value'],
            campaign = json['campaign']['value'],
            option =json['option']['value'],
            first_name = json['first_name']['value'],
            last_name = json['last_name']['value'],
            
            first_name_kata = json['first_name_kata']['value'],
            last_name_kata = json['last_name_kata']['value'],
            
            gender = json['gender']['value'],
            birthday = datetime.strptime(json['birthday']['value'], "%Y-%m-%d").date(),
            country = json['country']['value'],
            zip_code = json['zip_code']['value'],
            state_province = json['state_province']['value'],
            city = json['city']['value'],
            street = json['street']['value'],
            
            phone_number = json['phone_number']['value'],
            email = json['email']['value'],
            note = json['note']['value'],
            id = int(json['$id'].get('value')),
        )
        model.plan = json['plan']['value']
        return model
    
    
    
class Customer(models.Model):
    register_date = models.DateField()
    plan = models.TextField(default='')
    campaign = models.TextField(default='')
    option = models.TextField(default='')
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')
    
    first_name_kata = models.TextField(default='')
    last_name_kata = models.TextField(default='')
    
    gender = models.TextField(default='male')
    birthday = models.DateField()
    country = models.TextField(default='')
    zip_code = models.TextField(default='')
    state_province = models.TextField(default='')
    city = models.TextField(default='')
    street = models.TextField(default='')
    
    phone_number = models.TextField(default='')
    email = models.TextField(default='')
    note = models.TextField(default='')
    
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.plan
    
    def to_dict(self):
        return {
            'pk': self.pk,
            "register_date": self.register_date,
            "plan": self.plan,
            "campaign": self.campaign,
            "option": self.option,
            "first_name": self.first_name,
            "last_name": self.last_name,
            
            "first_name_kata": self.first_name_kata,
            "last_name_kata": self.last_name_kata,
            "gender": self.gender,
            "birthday": self.birthday,
            "country": self.country,
            "zip_code": self.zip_code,
            "state_province": self.state_province,
            "city": self.city,
            
            "street": self.street,
            "phone_number": self.phone_number,
            "email": self.email,
            "note": self.note,
            "created_date": self.created_date,
            "updated_date": self.updated_date,
            
        }
    
    # a = Customer(register_date="2024-01-15", plan="plan b", gender=True, birthday="2024-01-17")
    # a.save()
    
    
    
    