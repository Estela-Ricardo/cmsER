# Generated by Django 5.0.4 on 2024-05-02 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestatepro', '0011_alter_cliente_leidc_alter_propriedade_ano_construcao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propriedade',
            name='ano_construcao',
            field=models.IntegerField(blank=True, default=datetime.datetime(2024, 5, 2, 18, 7, 45, 840931, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
