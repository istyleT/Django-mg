# Generated by Django 4.1.2 on 2022-11-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellmg', '0006_alter_quotations_mainmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotations',
            name='filepdf',
            field=models.FileField(default='upload/django.pdf', upload_to='upload/'),
        ),
    ]