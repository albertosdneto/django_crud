# Generated by Django 2.2.6 on 2019-10-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_auto_20191020_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='company/default.png', upload_to='company/logo_pics'),
        ),
    ]