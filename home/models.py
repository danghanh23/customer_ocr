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
    
    # a = Customer(register_date="2024-01-15", plan="plan b", gender=True, birthday="2024-01-17")
    # a.save()