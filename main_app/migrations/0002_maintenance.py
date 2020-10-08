# Generated by Django 3.1.2 on 2020-10-08 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Maintenance date')),
                ('care', models.CharField(choices=[('W', 'Water'), ('F', 'Fertilize'), ('P', 'Prune')], default='W', max_length=1)),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.tree')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
