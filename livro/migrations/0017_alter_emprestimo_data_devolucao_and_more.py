# Generated by Django 4.1.4 on 2022-12-23 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0016_emprestimo_avaliacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 23, 9, 5, 10, 91510)),
        ),
    ]