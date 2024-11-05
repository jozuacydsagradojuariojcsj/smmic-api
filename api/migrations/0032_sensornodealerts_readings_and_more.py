# Generated by Django 5.0.2 on 2024-11-03 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_alter_smsensorreadings_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensornodealerts',
            name='readings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.smsensorreadings'),
        ),
        migrations.AlterField(
            model_name='sensornodealerts',
            name='alert_code',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
