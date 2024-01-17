from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
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
    username = forms.CharField(label='tai khoan', max_length=30)
    
    register_date = forms.DateField()
    plan = forms.CharField(label='plan')
    chamption = forms.CharField(label='chamption')
    option = forms.CharField(label='option')
    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='last_name')
    
    gender = forms.BooleanField()
    birthday = forms.DateField()
    country = forms.CharField(label='country')
    zip_code = forms.CharField(label='zip_code')
    state_province = forms.CharField(label='state_province')
    city = forms.CharField(label='city')
    street = forms.CharField(label='street')
    
    phone_number = forms.CharField(label='phone_number')
    email = forms.CharField(label='Email')
    note = forms.CharField(label='note')
    
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