from django import forms
from bapp.models import Category,Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Category_form(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'



class Blog_form(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','category','image','descriptions','blog_body','status','is_featured']


from django.contrib.auth.forms import UserCreationForm

class Authforms(UserCreationForm):

    class Meta:
        model =User
        fields = ['username','first_name','last_name','email','is_active','is_staff','is_superuser','groups','user_permissions','password1','password2']



class editform(forms.ModelForm):
    class Meta:
        model =User
        fields = ['username','first_name','last_name','email','is_active','is_staff','is_superuser','groups','user_permissions']

