from django.shortcuts import render, redirect
from .forms import MessageForm, ReservationForm


# Create your views here.
def home(request):
    all = AffordableModel.objects.all()
    template_name = 'index.html'
    category = AffordableModel.objects.all()
    context = {
        'all': all,
        'category': category
    }
    return render(request, template_name='index.html',context=context)


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


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
    else:
        form = ReservationForm()

    return render(request, 'index.html', {'form': form})
