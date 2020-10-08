from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Tree, Worker
from .forms import MaintenanceForm

# Add the following import

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def trees_index(request):
    trees = Tree.objects.all()
    return render(request, 'trees/index.html', { 'trees': trees })

def trees_detail(request, tree_id):
      tree = Tree.objects.get(id=tree_id)
      workers_tree_doesnt_have = Worker.objects.exclude(id__in = tree.workers.all().values_list('id'))
      maintenance_form = MaintenanceForm()
      return render(request, 'trees/detail.html', {
        'tree': tree, 'maintenance_form': maintenance_form,
        'workers': workers_tree_doesnt_have
    })

def add_maintenance(request, tree_id):
  form = MaintenanceForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.tree_id = tree_id
    new_maintenance.save()
  return redirect('detail', tree_id=tree_id)


def assoc_worker(request, tree_id, worker_id):
  Tree.objects.get(id=tree_id).workers.add(worker_id)
  return redirect('detail', tree_id=tree_id)

class TreeCreate(CreateView):
    model = Tree
    fields = '__all__'

class TreeUpdate(UpdateView):
    model = Tree
    fields = ['description', 'name']

class TreeDelete(DeleteView):
    model = Tree
    success_url = '/trees/'

class WorkerList(ListView):
      model = Worker

class WorkerDetail(DetailView):
  model = Worker

class WorkerCreate(CreateView):
  model = Worker
  fields = '__all__'
class WorkerUpdate(UpdateView):
  model = Worker
  fields = ['name', 'age']

class WorkerDelete(DeleteView):
  model = Worker
  success_url = '/workers/'