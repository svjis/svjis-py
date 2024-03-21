# Generated by Django 5.0.3 on 2024-03-21 12:05

import articles.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FaultReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('slug', models.CharField(max_length=50)),
                ('description', models.TextField(verbose_name='Description')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False, verbose_name='Closed')),
                ('assigned_to_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_fault_set', to=settings.AUTH_USER_MODEL)),
                ('created_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('entrance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.buildingentrance', verbose_name='Entrance')),
                ('watching_users', models.ManyToManyField(related_name='watching_fault_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'permissions': (('svjis_view_fault_menu', 'Can view Faults menu'), ('svjis_fault_reporter', 'Can report fault'), ('svjis_fault_resolver', 'Can resolve fault')),
            },
        ),
        migrations.CreateModel(
            name='FaultComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(verbose_name='Body')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fault_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.faultreport', verbose_name='Fault report')),
            ],
            options={
                'ordering': ['-id'],
                'permissions': (('svjis_add_fault_comment', 'Can add Fault comment'),),
            },
        ),
        migrations.CreateModel(
            name='FaultAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('file', models.FileField(upload_to=articles.models.fault_directory_path, verbose_name='File')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('fault_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.faultreport', verbose_name='Fault report')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
