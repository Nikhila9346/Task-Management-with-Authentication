from django.shortcuts import render
from .models import Task
# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        Task.objects.create(
            name = name,
            desc = desc,
            user = request.user
        )

    tasks = Task.objects.filter(user=request.user).order_by('-id')
    context = {
        'tasks':tasks
    }
    return render(request, 'home.html', context)