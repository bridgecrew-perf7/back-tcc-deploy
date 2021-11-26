# Generated by Django 3.1.1 on 2021-01-07 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reclamacoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamacao',
            name='status',
            field=models.IntegerField(choices=[(1, 'Aberta'), (2, 'Julgada Vitória'), (3, 'Julgada Derrota')], default=1),
        ),
    ]
