# Generated by Django 3.2.5 on 2021-08-19 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.IntegerField(blank=True, max_length=20, null=True, unique=True)),
                ('nominee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll_simulator.candidates')),
            ],
        ),
    ]
