# Generated by Django 3.1 on 2021-04-08 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vessel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('equipment_code', models.CharField(max_length=8, unique=True, verbose_name='Equipment Code')),
                ('location', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('vessel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vessel.vessel')),
            ],
            options={
                'verbose_name': 'Equipment',
                'verbose_name_plural': 'Equipments',
            },
        ),
    ]
