# Generated by Django 4.1 on 2022-09-11 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_upcheck_username_alter_upcheck_up_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcheck',
            name='up_check',
        ),
    ]
