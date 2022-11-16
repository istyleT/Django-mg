# Generated by Django 4.1.2 on 2022-11-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellmg', '0005_quotations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotations',
            name='mainmodel',
            field=models.CharField(choices=[('MG5', 'MG 5'), ('MGVSHEV', 'MG VS HEV'), ('MGZS', 'MG ZS'), ('MGEDT', 'MG EXTENDER'), ('MGHSPHEV', 'MG HS PHEV'), ('MGHS', 'MG HS')], default='MG5', max_length=15),
        ),
    ]