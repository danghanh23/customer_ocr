from django.db import models
from django.utils import timezone
# Create your models here.
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