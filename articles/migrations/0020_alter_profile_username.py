# Generated by Django 4.1 on 2022-09-14 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
