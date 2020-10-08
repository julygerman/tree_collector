from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('trees/', views.trees_index, name='index'),
  path('trees/<int:tree_id>', views.trees_detail, name='detail'),
  path('trees/create/', views.TreeCreate.as_view(), name='trees_create'),
  path('trees/<int:pk>/update', views.TreeUpdate.as_view(), name='trees_update'),
  path('trees/<int:pk>/delete', views.TreeDelete.as_view(), name='trees_delete'),
  path('trees/<int:tree_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
  path('workers/', views.WorkerList.as_view(), name='workers_index'),
  path('workers/<int:pk>/', views.WorkerDetail.as_view(), name='workers_detail'),
  path('workers/create/', views.WorkerCreate.as_view(), name='workers_create'),
  path('workers/<int:pk>/update/', views.WorkerUpdate.as_view(), name='workers_update'),
  path('workers/<int:pk>/delete/', views.WorkerDelete.as_view(), name='workers_delete'),
  path('trees/<int:tree_id>/assoc_worker/<int:worker_id>/', views.assoc_worker, name='assoc_worker'),
]