from django.db import models
from django.utils import timezone
# Create your models here.
from datetime import datetime

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
    
    
    
    