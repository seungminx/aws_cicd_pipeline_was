# Generated by Django 3.1.14 on 2023-11-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password1',
            field=models.CharField(max_length=100),
        ),
    ]
