# Generated by Django 5.0.2 on 2024-08-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_sink_node_sk_name_sink_node_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sink_node',
            name='SK_Name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
