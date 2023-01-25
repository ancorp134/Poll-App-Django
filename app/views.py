from django.shortcuts import render , redirect
from .forms import QuestionForm , RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Question

# Create your views here.


def Home(request):
    question = Question.objects.all()

    context = {'question' : question}

    return render(request , 'base.html' , context)


def register_user(request):
    registration_form =  RegistrationForm()

    if request.method == 'POST' :
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()

    return render(request , 'register.html' , {'registration_form' : registration_form})


@login_required
def Create_Poll(request):
    
    
    
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            # return redirect('home')
    return render(request, 'create_poll.html', {'form': form})
    
    
@login_required
def profile_view(request):
    
    question = Question.objects.filter(user = request.user)


    return render(request , 'accounts/profile.html' , {'question' : question})
