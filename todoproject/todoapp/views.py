from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task1
from . forms import TodoForm
from django.views.generic import ListView
from django. views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from . import views

class TaskListview(ListView):
    model=Task1
    template_name='home.html'
    context_object_name='task'

class TaskDetailview(DetailView):
    model=Task1
    template_name='detail.html'
    context_object_name='task'


class TaskUpdateview(UpdateView):
    model=Task1
    template_name='update.html'
    context_object_name='task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):
    model=Task1
    template_name='delete.html'

    def get_success_url(self):
        return reverse_lazy('cbvhome')

# Create your views here.
def add(request):

    task1 = Task1.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority', '')
        date=request.POST.get('date','')
        task=Task1(name=name,priority=priority,date=date)

        task.save()
    return render(request, 'home.html',{'task':task1})

#def details(request):

    #task1=Task1.objects.all()
    #return render(request,'details.html',{'task':task1})

def delete(request,tasksid):
    tasks=Task1.objects.get(id=tasksid)
    if request.method=='POST':
        tasks.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    t=Task1.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=t)
    if f. is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f':f,'t':t})

