from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Tree, Worker
from .forms import MaintenanceForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Add the following import

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def trees_index(request):
    trees = request.user.tree_set.all()
    return render(request, 'trees/index.html', { 'trees': trees })

@login_required
def trees_detail(request, tree_id):
      tree = Tree.objects.get(id=tree_id)
      workers_tree_doesnt_have = Worker.objects.exclude(id__in = tree.workers.all().values_list('id'))
      maintenance_form = MaintenanceForm()
      return render(request, 'trees/detail.html', {
        'tree': tree, 'maintenance_form': maintenance_form,
        'workers': workers_tree_doesnt_have
    })

@login_required
def add_maintenance(request, tree_id):
  form = MaintenanceForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.tree_id = tree_id
    new_maintenance.save()
  return redirect('detail', tree_id=tree_id)


@login_required
def assoc_worker(request, tree_id, worker_id):
  Tree.objects.get(id=tree_id).workers.add(worker_id)
  return redirect('detail', tree_id=tree_id)


def signup(request):
      error_message = ''
      if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
          user = form.save()
          login(request, user)
          return redirect('index')
        else:
          error_message = 'Invalid sign up - try again'
      form = UserCreationForm()
      context = {'form': form, 'error_message': error_message}
      return render(request, 'registration/signup.html', context)


class TreeCreate(CreateView):
    model = Tree
    fields = '__all__'
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class TreeUpdate(UpdateView, LoginRequiredMixin):
    model = Tree
    fields = ['description', 'name']

class TreeDelete(DeleteView, LoginRequiredMixin):
    model = Tree
    success_url = '/trees/'

class WorkerList(ListView, LoginRequiredMixin):
      model = Worker

class WorkerDetail(DetailView, LoginRequiredMixin):
  model = Worker

class WorkerCreate(CreateView, LoginRequiredMixin):
  model = Worker
  fields = '__all__'
class WorkerUpdate(UpdateView, LoginRequiredMixin):
  model = Worker
  fields = ['name', 'age']

class WorkerDelete(DeleteView, LoginRequiredMixin):
  model = Worker
  success_url = '/workers/'