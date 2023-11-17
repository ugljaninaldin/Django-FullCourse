# Generated by Django 4.2.7 on 2023-11-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_guide', '0012_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('O', 'Other'), ('F', 'Female')], default='M', max_length=1, verbose_name='Pol'),
        ),
    ]