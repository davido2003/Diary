from django.shortcuts import redirect, render
from . models import Entry
from . form import Entryform
# Create your views here.
def web1(request):
    post = Entry.objects.order_by('-date_posted')
    return render(request, 'index.html', {'post':post})

def web2(request):
    if request.method == 'POST':
        form = Entryform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Entryform()
        return render(request, 'add.html', {'form':form})