# Generated by Django 4.1.2 on 2022-11-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellmg', '0004_colorsubmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('username', models.CharField(max_length=20)),
                ('mainmodel', models.CharField(max_length=20)),
                ('filepdf', models.FileField(upload_to='')),
            ],
        ),
    ]
