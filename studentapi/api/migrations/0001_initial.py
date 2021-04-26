# Generated by Django 2.2 on 2021-04-25 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('standard', models.CharField(choices=[('One', 'One'), ('Two', 'Two'), ('Three', 'Three'), ('Four', 'Four'), ('Five', 'Five'), ('Six', 'Six'), ('Seven', 'Seven'), ('Eight', 'Eight'), ('Nine', 'Nine'), ('Ten', 'Ten')], max_length=50)),
                ('evaluation', models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail')], max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('active', models.BooleanField(blank=True)),
                ('joined_on', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('relation', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Other', 'Other')], max_length=50)),
                ('address', models.TextField(blank=True)),
                ('mobile_number', models.PositiveIntegerField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Student')),
            ],
        ),
    ]
