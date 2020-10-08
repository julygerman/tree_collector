from django.contrib import admin
from .models import Tree, Maintenance, Worker

# Register your models here.
admin.site.register(Tree)
admin.site.register(Maintenance)
admin.site.register(Worker)