# Generated by Django 2.2 on 2021-04-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210425_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardian',
            name='relation',
            field=models.CharField(choices=[('father', 'Father'), ('father', 'Mother'), ('other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='evaluation',
            field=models.CharField(choices=[('pass', 'Pass'), ('fail', 'Fail')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='standard',
            field=models.CharField(choices=[('one', 'One'), ('two', 'Two'), ('three', 'Three'), ('four', 'Four'), ('five', 'Five'), ('six', 'Six'), ('seven', 'Seven'), ('eight', 'Eight'), ('nine', 'Nine'), ('ten', 'Ten')], max_length=50),
        ),
    ]
