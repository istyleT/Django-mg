# Generated by Django 4.1.4 on 2022-12-14 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellmg', '0015_alter_htrcustomer_chanelcustomer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pathstatushtr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_htrcustomer', models.CharField(max_length=3)),
                ('date', models.DateField(auto_now_add=True)),
                ('statuscustomer', models.CharField(max_length=30)),
                ('remark', models.CharField(default='-', max_length=100)),
            ],
        ),
    ]
