# Generated by Django 4.1 on 2022-10-04 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellmg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regiscosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regis_code', models.CharField(max_length=30)),
                ('regis_company', models.IntegerField()),
                ('regis_personal', models.IntegerField()),
            ],
        ),
    ]
