from django.shortcuts import render , redirect
from .forms import QuestionForm

# Create your views here.


def Create_Poll(request):
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create_poll.html', {'form': form})
    
    
