from django.db import models

# Create your models here.
class Customer(models.Model):
    register_date = models.DateField()
    plan = models.TextField()
    chamption = models.TextField()
    option = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    
    gender = models.BooleanField()
    birthday = models.DateField()
    country = models.TextField()
    zip_code = models.TextField()
    state_province = models.TextField()
    city = models.TextField()
    street = models.TextField()
    
    phone_number = models.TextField()
    email = models.TextField()
    note = models.TextField()

    def __str__(self):
        return self.plan
    
    # a = Customer(register_date="2024-01-15", plan="plan b", gender=True, birthday="2024-01-17")
    # a.save()