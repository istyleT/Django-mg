# Generated by Django 4.1.2 on 2022-11-12 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellmg', '0008_alter_quotations_filepdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotations',
            name='filepdf',
            field=models.FileField(upload_to='upload/'),
        ),
    ]
