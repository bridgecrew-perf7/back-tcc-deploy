# Generated by Django 3.1.1 on 2021-01-07 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamentos', '0004_solicitacaosaque_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacaosaque',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]