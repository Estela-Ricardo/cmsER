# Generated by Django 5.0.4 on 2024-05-02 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestatepro', '0004_alter_propriedade_ano_construcao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propriedade',
            name='ano_construcao',
            field=models.IntegerField(blank=True, default=datetime.datetime(2024, 5, 2, 15, 41, 29, 953797, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
