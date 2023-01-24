from django import forms
from .models import Question , CustomUser

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'choice1', 'choice2', 'choice3', 'choice4']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name' , 'email' , 'password' , 'phone_num'] 

