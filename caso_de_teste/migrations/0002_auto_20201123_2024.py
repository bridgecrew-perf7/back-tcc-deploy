# Generated by Django 3.1.1 on 2020-11-23 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caso_de_teste', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casodeteste',
            name='data_execucao',
            field=models.DateField(blank=True, null=True),
        ),
    ]
