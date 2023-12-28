from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import DocumentaryForm  # Replace with your forms
from .models import Documentary, Resource  # Replace with your models
# Create your views here.


def documentary_list(request):
    documentaries = Documentary.objects.all()
    context = {
        'documentaries': documentaries,
    }
    return render(request, 'adminapp/index.html', context)

def documentary_detail(request, pk):
    documentary = Documentary.objects.get(pk=pk)
    context = {
        'documentary': documentary,
    }
    return render(request, 'adminapp/detail.html', context)


def documentary_create(request):
    if request.method == 'POST':
        form = DocumentaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('documentary_list')
    else:
        form = DocumentaryForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/create.html', context)

# Similar views for other model creation and update with appropriate forms
