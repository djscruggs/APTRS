# Generated by Django 4.1.7 on 2023-03-16 14:28

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('scope', models.CharField(default=None, max_length=100)),
                ('description', models.CharField(default=None, max_length=1000)),
                ('projecttype', models.CharField(default=None, max_length=100)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('testingtype', models.CharField(default='White Box', max_length=100)),
                ('projectexception', models.CharField(blank=True, max_length=1000, null=True)),
                ('companyname', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='customers.company')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vulnerabilityname', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('vulnerabilityseverity', models.CharField(max_length=300, null=True)),
                ('cvssscore', models.FloatField(blank=True, null=True)),
                ('cvssvector', models.CharField(default=None, max_length=300, null=True)),
                ('status', models.CharField(choices=[('Vulnerable', 'Vulnerable'), ('Confirm Fixed', 'Confirm Fixed'), ('Accepted Risk', 'Accepted Risk')], default='Vulnerable', max_length=20)),
                ('vulnerabilitydescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('POC', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('vulnerabilitysolution', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('vulnerabilityreferlnk', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'unique_together': {('project', 'vulnerabilityname')},
            },
        ),
        migrations.CreateModel(
            name='Vulnerableinstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('Paramter', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('status', models.CharField(choices=[('Vulnerable', 'Vulnerable'), ('Confirm Fixed', 'Confirm Fixed'), ('Accepted Risk', 'Accepted Risk')], default='Vulnerable', max_length=20)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('vulnerabilityid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='project.vulnerability')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRetest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
    ]
