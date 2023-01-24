from django.shortcuts import render , redirect
from .forms import QuestionForm , RegistrationForm

# Create your views here.



def register_user(request):
    registration_form =  RegistrationForm()

    if request.method == 'POST' :
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()

    return render(request , 'register.html' , {'registration_form' : registration_form})



def Create_Poll(request):
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home')
    return render(request, 'create_poll.html', {'form': form})
    
    
