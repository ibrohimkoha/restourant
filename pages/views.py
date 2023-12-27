from django.shortcuts import render, redirect
from .forms import MessageForm
# Create your views here.
def home(request):
    return render(request, template_name='index.html')

def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            return render(request, template_name='index.html')
    else:
        return render(request, template_name='index.html')