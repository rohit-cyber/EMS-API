# Generated by Django 2.2.12 on 2021-05-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210426_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardian',
            name='relation',
            field=models.CharField(choices=[('father', 'Father'), ('mother', 'Mother'), ('other', 'Other')], max_length=50),
        ),
    ]
