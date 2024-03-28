# Generated by Django 5.0.3 on 2024-03-28 20:58

import articles.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
            ],
            options={
                'ordering': ['description'],
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
            name='BuildingUnitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
            ],
            options={
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Name')),
                ('address', models.CharField(blank=True, max_length=50, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='City')),
                ('post_code', models.CharField(blank=True, max_length=10, verbose_name='Post code')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Phone')),
                ('email', models.CharField(blank=True, max_length=50, verbose_name='E-Mail')),
                ('registration_no', models.CharField(blank=True, max_length=20, verbose_name='Registration no.')),
                ('vat_registration_no', models.CharField(blank=True, max_length=20, verbose_name='VAT Registration no.')),
                ('internet_domain', models.CharField(blank=True, max_length=50, verbose_name='Internet domain')),
                ('header_picture', models.FileField(blank=True, null=True, upload_to=articles.models.company_directory_path, verbose_name='Header picture (940 x 94)')),
            ],
            options={
                'permissions': (('svjis_edit_admin_company', 'Can edit Company'),),
            },
        ),
        migrations.CreateModel(
            name='MessageQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, verbose_name='E-Mail')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('body', models.TextField(verbose_name='Body')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('sending_time', models.DateTimeField(null=True)),
                ('status', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, verbose_name='Key')),
                ('value', models.CharField(max_length=1000, verbose_name='Value')),
            ],
            options={
                'permissions': (('svjis_edit_admin_preferences', 'Can edit Preferences'),),
            },
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50, verbose_name='Header')),
                ('body', models.TextField(verbose_name='Body')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Phone')),
                ('email', models.CharField(blank=True, max_length=50, verbose_name='E-Mail')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('created_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.adverttype', verbose_name='Type')),
            ],
            options={
                'ordering': ['-id'],
                'permissions': (('svjis_view_adverts_menu', 'Can view Adverts menu'), ('svjis_add_advert', 'Can add Advert')),
            },
        ),
        migrations.CreateModel(
            name='AdvertAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('file', models.FileField(upload_to=articles.models.advert_directory_path, verbose_name='File')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.advert', verbose_name='Advert')),
                ('created_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, verbose_name='Header')),
                ('slug', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('perex', models.TextField(verbose_name='Perex')),
                ('body', models.TextField(verbose_name='Body')),
                ('allow_comments', models.BooleanField(default=False, verbose_name='Allow comments')),
                ('visible_for_all', models.BooleanField(default=False, verbose_name='Visible for all')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visible_for_group', models.ManyToManyField(to='auth.group')),
                ('watching_users', models.ManyToManyField(related_name='watching_article_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'permissions': (('svjis_view_redaction_menu', 'Can view Redaction menu'), ('svjis_edit_article', 'Can edit Article')),
            },
        ),
        migrations.CreateModel(
            name='ArticleAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('file', models.FileField(upload_to=articles.models.article_directory_path, verbose_name='File')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='Article')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(verbose_name='Body')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='Article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'permissions': (('svjis_add_article_comment', 'Can add Article comment'),),
            },
        ),
        migrations.CreateModel(
            name='ArticleLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('hide', models.BooleanField(default=False, verbose_name='Hide')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.articlemenu')),
            ],
            options={
                'ordering': ['description'],
                'permissions': (('svjis_edit_article_menu', 'Can edit Menu'),),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articlemenu'),
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
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.buildingunittype', verbose_name='Type')),
            ],
            options={
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField(verbose_name='Order')),
                ('position', models.CharField(max_length=30, verbose_name='Position')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.company', verbose_name='Company')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
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
                ('created_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fault_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.faultreport', verbose_name='Fault report')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('body', models.TextField(verbose_name='Body')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'permissions': (('svjis_edit_article_news', 'Can edit News'),),
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
                ('starting_date', models.DateField(verbose_name='Starting day')),
                ('ending_date', models.DateField(verbose_name='Ending day')),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'permissions': (('svjis_answer_survey', 'Can answer Survey'), ('svjis_edit_survey', 'Can edit Survey')),
            },
        ),
        migrations.CreateModel(
            name='SurveyOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.survey')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SurveyAnswerLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.survey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.surveyoption')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(blank=True, max_length=30, verbose_name='Salutation')),
                ('address', models.CharField(blank=True, max_length=50, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='City')),
                ('post_code', models.CharField(blank=True, max_length=10, verbose_name='Post code')),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='Country')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Phone')),
                ('show_in_phonelist', models.BooleanField(default=False, verbose_name='Show in phonelist')),
                ('internal_note', models.CharField(blank=True, max_length=250, verbose_name='Internal note')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('svjis_view_admin_menu', 'Can view Administration menu'), ('svjis_edit_admin_users', 'Can edit Users'), ('svjis_edit_admin_groups', 'Can edit Groups'), ('svjis_view_personal_menu', 'Can view Personal settings menu'), ('svjis_view_phonelist', 'Can view Phonelist')),
            },
        ),
    ]
