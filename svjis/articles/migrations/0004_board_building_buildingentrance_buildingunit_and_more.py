# Generated by Django 5.0.2 on 2024-03-12 21:23

import articles.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_buliding_company_messagequeue_preferences'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField(verbose_name='Order')),
                ('position', models.CharField(max_length=30, verbose_name='Position')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=50, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='City')),
                ('post_code', models.CharField(blank=True, max_length=10, verbose_name='Post code')),
                ('land_registry_no', models.CharField(blank=True, max_length=50, verbose_name='Land Registration no.')),
            ],
            options={
                'permissions': (('svjis_edit_admin_building', 'Can edit Building'),),
            },
        ),
        migrations.CreateModel(
            name='BuildingEntrance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.building', verbose_name='Building')),
            ],
            options={
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='BuildingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_id', models.CharField(max_length=50, verbose_name='Registration Id')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
                ('numerator', models.IntegerField(verbose_name='Numerator')),
                ('denominator', models.IntegerField(verbose_name='Denominator')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.building', verbose_name='Building')),
                ('entrance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.buildingentrance', verbose_name='Entrance')),
                ('owners', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='BuildingUnitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
            ],
            options={
                'ordering': ['description'],
            },
        ),
        migrations.DeleteModel(
            name='Buliding',
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('svjis_view_admin_menu', 'Can view Administration menu'), ('svjis_edit_admin_users', 'Can edit Users'), ('svjis_edit_admin_groups', 'Can edit Groups'), ('svjis_view_personal_menu', 'Can view Personal settings menu'), ('svjis_view_phonelist', 'Can view Phonelist'))},
        ),
        migrations.AddField(
            model_name='company',
            name='header_picture',
            field=models.FileField(blank=True, null=True, upload_to=articles.models.company_directory_path, verbose_name='Header picture (940 x 94)'),
        ),
        migrations.AddField(
            model_name='board',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='board',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buildingunit',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.buildingunittype', verbose_name='Type'),
        ),
    ]
