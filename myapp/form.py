from django import forms
from .models import UserData, form_user_data, movie_info

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['firstname','lastname']


class form_user(forms.ModelForm):
    class Meta:
        model = form_user_data
        fields = ['name','age','marital_status','nationality','gender','language'] 

class movie_form(forms.ModelForm):
    class Meta:
        model = movie_info
        fields = ['title','year','desc']

