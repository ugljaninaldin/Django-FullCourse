# Generated by Django 4.2.7 on 2023-11-17 19:43

from django.db import migrations, models
import models_guide4.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('even_int', models.IntegerField(validators=[models_guide4.models.int_is_evean])),
            ],
        ),
    ]
