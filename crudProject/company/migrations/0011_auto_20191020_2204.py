# Generated by Django 2.2.6 on 2019-10-20 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20191020_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='company/default.jpeg', upload_to='company/logo_pics'),
        ),
    ]
