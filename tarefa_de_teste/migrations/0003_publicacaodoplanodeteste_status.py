# Generated by Django 3.1.1 on 2020-12-16 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa_de_teste', '0002_execucaoteste_manifestacaointeresse'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacaodoplanodeteste',
            name='status',
            field=models.IntegerField(choices=[(1, 'Não Publicado'), (2, 'Publicado'), (3, 'Pausado')], default=1),
        ),
    ]
