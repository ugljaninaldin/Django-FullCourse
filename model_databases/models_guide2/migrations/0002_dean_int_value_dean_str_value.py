# Generated by Django 4.2.7 on 2023-11-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_guide2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dean',
            name='int_value',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='dean',
            name='str_value',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
