from django import forms
from .models import Question , CustomUser
from django.contrib.auth.forms import AuthenticationForm

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'choice1', 'choice2', 'choice3', 'choice4']


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label = 'password' , widget = forms.PasswordInput(attrs= {'class' : 'form-control'}))
    class Meta:
        model = CustomUser
        fields = ['name' , 'email','phone_num','password'] 


class LoginForm(AuthenticationForm):
    # email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label = 'password' , widget = forms.PasswordInput(attrs= {'class' : 'form-control'}))
