# Generated by Django 4.1 on 2022-09-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0021_alter_profile_icon_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itembox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('icon_id', models.IntegerField(default=0)),
            ],
        ),
    ]
