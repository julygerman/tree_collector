from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
CARE = (
    ('W', 'Water'),
    ('F', 'Fertilize'),
    ('P', 'Prune')
)

class Worker(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('workers_detail', kwargs={'pk': self.id})

class Tree(models.Model):
    name = models.CharField(max_length=250)
    tree_type = models.CharField(max_length=250)
    soil_Preferences = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    attributes = models.CharField(max_length=250)
    image = models.URLField()
    workers = models.ManyToManyField(Worker)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'tree_id': self.id})
    def cared_for_today(self):
        return self.maintenance_set.filter(date=date.today()).count() >= len(CARE)


class Maintenance(models.Model):
    date = models.DateField('Maintenance date')
    care = models.CharField(
    max_length=1, 
    choices=CARE, 
    default=CARE[0][0])

    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_care_display()} on {self.date}"
        
    class Meta:
        ordering = ['-date']