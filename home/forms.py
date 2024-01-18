from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from home.models import Customer
class RegistrationForm(forms.Form):
    username = forms.CharField(label='tai khoan', max_length=30)
    email = forms.CharField(label='Email')
    password1 = forms.CharField(label='mat khau', widget=forms.PasswordInput())
    password2 = forms.CharField(label='nhap lai mat khau', widget=forms.PasswordInput())
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("mat khau khong hop le")
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("username co ky tu dac biet")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("tai khoan da ton tai")
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'] )
        
        
        
class CustomerForm(forms.Form):
    register_date = forms.DateField()
    plan = forms.CharField(label='plan')
    campaign = forms.CharField(label='campaign')
    option = forms.CharField(label='option')
    
    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='last_name')
    first_name_kata = forms.CharField(label='first_name_kata')
    last_name_kata = forms.CharField(label='last_name_kata')
    
    gender = forms.CharField(label='gender')
    birthday = forms.DateField()
    
    country = forms.CharField(label='country')
    zip_code = forms.CharField(label='zip_code')
    state_province = forms.CharField(label='state_province')
    city = forms.CharField(label='city')
    street = forms.CharField(label='street')
    
    phone_number = forms.CharField(label='phone_number')
    email = forms.CharField(label='email')
    note = forms.CharField(label='note')
    
    # def clean_password2(self):
    #     if 'password1' in self.cleaned_data:
    #         password1 = self.cleaned_data['password1']
    #         password2 = self.cleaned_data['password2']
    #         if password1 == password2 and password1:
    #             return password2
    #     raise forms.ValidationError("mat khau khong hop le")
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if not re.search(r'^\w+$', username):
    #         raise forms.ValidationError("username co ky tu dac biet")
    #     try:
    #         User.objects.get(username=username)
    #     except ObjectDoesNotExist:
    #         return username
    #     raise forms.ValidationError("tai khoan da ton tai")
    # def save(self):
    #     customer = Customer(
    #         register_date = self.cleaned_data['register_date'],
    #         plan = self.cleaned_data['plan'],
    #         campaign = self.cleaned_data['campaign'],
    #         option = self.cleaned_data['option'],
    #         first_name = self.cleaned_data['first_name'],
    #         last_name = self.cleaned_data['last_name'],
            
    #         gender = self.cleaned_data['gender'],
    #         birthday = self.cleaned_data['birthday'],
    #         country = self.cleaned_data['country'],
    #         zip_code = self.cleaned_data['zip_code'],
    #         state_province = self.cleaned_data['state_province'],
    #         city = self.cleaned_data['city'],
    #         street = self.cleaned_data['street'],
            
    #         phone_number = self.cleaned_data['phone_number'],
    #         email = self.cleaned_data['email'],
    #         note = self.cleaned_data['note'],
    #         )
    #     customer.save()