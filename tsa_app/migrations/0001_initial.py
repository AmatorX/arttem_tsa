# Generated by Django 5.0.3 on 2024-03-16 17:45

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('total_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=22, null=True)),
                ('sh_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('build_obj', models.ManyToManyField(related_name='materials', to='tsa_app.buildobject')),
            ],
        ),
        migrations.AddField(
            model_name='buildobject',
            name='material',
            field=models.ManyToManyField(related_name='build_objects', to='tsa_app.material'),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tg_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('foreman', models.BooleanField(default=False)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('employment_agreement', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('NA', 'N/A')], default='NA', max_length=3)),
                ('over_time', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('NA', 'N/A')], default='NA', max_length=3)),
                ('start_to_work', models.DateField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payroll_eligible', models.DateField(blank=True, null=True)),
                ('payroll', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('NA', 'N/A')], default='NA', max_length=3)),
                ('resign_agreement', models.DateField(blank=True, null=True)),
                ('benefits_eligible', models.DateField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(99)])),
                ('issued', models.DateField(blank=True, null=True)),
                ('expiry', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=35, null=True)),
                ('tickets_available', models.CharField(blank=True, max_length=255, null=True)),
                ('build_obj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workers', to='tsa_app.buildobject')),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('tool_id', models.CharField(blank=True, max_length=255, unique=True)),
                ('date_of_issue', models.DateField(blank=True, null=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tools', to='tsa_app.worker')),
            ],
        ),
    ]
